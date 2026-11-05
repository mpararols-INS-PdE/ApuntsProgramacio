#!/usr/bin/env python3
"""Exporta el temario actual a EPUB o DOCX con Python 3.9+ y Pandoc 3.x."""

import argparse
import importlib.util
from pathlib import Path
import re
import shutil
import subprocess
import tempfile

ROOT = Path(__file__).resolve().parents[1]
BASE = '/ApuntsProgramacio/'
SITE = 'https://mpararols-ins-pde.github.io' + BASE
LANGUAGES = {
    'es': ('Apuntes de programación Java', 'es-ES', 'cast', 'portada.png'),
    'va': ('Apunts de programació Java', 'ca-ES-valencia', 'val', 'portada_val.png'),
    'ca': ('Apunts de programació Java', 'ca-ES', 'ca', 'portada_val.png'),
}
BULLETINS = ('inicial', 'inicial-resuelto', 'avanzado', 'avanzado-resuelto', 'extras')
FENCES = re.compile(r'(?ms)^([ \t]*)(`{3,}|~{3,})[^\n]*\n.*?^\1\2[ \t]*(?:\n|$)')


def outside_code(text, transform):
    parts, previous = [], 0
    for match in FENCES.finditer(text):
        parts.extend((transform(text[previous:match.start()]), match[0]))
        previous = match.end()
    parts.append(transform(text[previous:]))
    return ''.join(parts)


def document(path, level, root, work, output_format):
    text = path.read_text(encoding='utf-8-sig')
    frontmatter = re.match(r'\A---\s*\n(.*?)\n---\s*\n', text, re.S)
    if not frontmatter:
        raise ValueError(f'Falta el frontmatter: {path}')
    title = re.search(r'^title:\s*(.+)$', frontmatter[1], re.M)
    if not title:
        raise ValueError(f'Falta el título: {path}')
    title = title[1].strip().strip('"\'')
    body = re.sub(r'\A# [^\n]+\n+', '', text[frontmatter.end():].strip())

    def transform(part):
        part = re.sub(r'(?m)^(#{1,6}) ', lambda m: '#' * min(6, len(m[1]) + level - 1) + ' ', part)
        part = re.sub(r'<details[^>]*>\s*<summary>(.*?)</summary>', r'\n\n**\1**\n\n', part, flags=re.S)
        part = part.replace('</details>', '\n')

        def image(match):
            asset = root / 'public' / match[2]
            if not asset.is_file():
                raise FileNotFoundError(f'Imagen de {path}: {asset}')
            if output_format == 'docx' and asset.suffix == '.svg':
                target = work / (asset.stem + '.png')
                if not target.exists():
                    if shutil.which('rsvg-convert'):
                        subprocess.run(['rsvg-convert', '-z', '2', '-o', str(target), str(asset)], check=True)
                    elif importlib.util.find_spec('cairosvg'):
                        import cairosvg
                        cairosvg.svg2png(url=str(asset), write_to=str(target), scale=2)
                    else:
                        raise RuntimeError('Los DOCX con SVG requieren rsvg-convert o Python con cairosvg.')
                asset = target
            return f'![{match[1]}](<{asset.as_posix()}>)'

        part = re.sub(r'!\[([^\]]*)\]\(' + re.escape(BASE) + r'([^)]+)\)', image, part)
        part = re.sub(r'(?<!!)\]\(' + re.escape(BASE), '](' + SITE, part)
        return part.replace('href="' + BASE, 'href="' + SITE)

    return '#' * level + ' ' + title + '\n\n' + outside_code(body, transform) + '\n'


def unit_files(docs):
    for folder in sorted(docs.iterdir()):
        if not folder.is_dir() or not re.match(r'^\d{2}-', folder.name):
            continue
        index = docs / (folder.name + '.md')
        if not index.is_file():
            index = folder / 'index.md'
        if not index.is_file():
            raise FileNotFoundError(f'Falta el índice de {folder}')
        chapters = sorted(p for p in folder.glob('*.md') if p.name != 'index.md')
        bulletins = [docs / 'boletines' / f'boletin-u{folder.name[:2]}-{kind}.md' for kind in BULLETINS]
        yield folder.name, index, chapters, [p for p in bulletins if p.is_file()]


def export(root, language, output_format, out_dir):
    docs = root / 'src/content/docs'
    if language != 'es':
        docs /= language
    title, lang_tag, suffix, cover = LANGUAGES[language]
    if not docs.is_dir():
        raise FileNotFoundError(docs)
    with tempfile.TemporaryDirectory(prefix='apuntes-export-') as tmp:
        work = Path(tmp)

        def pandoc(text, target, toc):
            source = work / 'document.md'
            source.write_text(text, encoding='utf-8')
            target.parent.mkdir(parents=True, exist_ok=True)
            command = ['pandoc', str(source), '--from=gfm', '--to=' + ('epub3' if output_format == 'epub' else 'docx'),
                       '--metadata=title:' + title, '--metadata=author:Sergi Garcia Barea',
                       '--metadata=lang:' + lang_tag, '--highlight-style=pygments', '-o', str(target)]
            if toc:
                command += ['--toc', '--toc-depth=2']
            if output_format == 'epub':
                command += ['--epub-cover-image=' + str(root / 'public' / cover), '--css=' + str(root / 'scripts/epub.css')]
            subprocess.run(command, cwd=root, check=True)
            print(target.relative_to(root) if target.is_relative_to(root) else target)

        course = []
        for name, index, chapters, bulletins in unit_files(docs):
            unit = document(index, 1, root, work, output_format) + '\n\n' + '\n\n'.join(
                document(p, 2, root, work, output_format) for p in chapters)
            if output_format == 'docx':
                folder = out_dir / language / name
                pandoc(unit, folder / (name + '.docx'), True)
                for bulletin in bulletins:
                    pandoc(document(bulletin, 1, root, work, output_format), folder / (bulletin.stem + '.docx'), False)
            else:
                course.append(unit)
                course.extend(document(p, 2, root, work, output_format) for p in bulletins)
        if output_format == 'epub':
            pandoc('\n\n'.join(course), out_dir / f'ApuntesProgramacion-{suffix}.epub', True)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--format', choices=('epub', 'docx'), required=True)
    parser.add_argument('--lang', choices=(*LANGUAGES, 'all'), default='es')
    parser.add_argument('--root', type=Path, default=ROOT)
    parser.add_argument('--out-dir', type=Path)
    args = parser.parse_args()
    if not shutil.which('pandoc'):
        parser.error('Se requiere Pandoc 3.x en PATH.')
    root = args.root.resolve()
    out_dir = args.out_dir or Path('public/epub' if args.format == 'epub' else 'docx')
    if not out_dir.is_absolute():
        out_dir = root / out_dir
    for language in LANGUAGES if args.lang == 'all' else (args.lang,):
        export(root, language, args.format, out_dir)


if __name__ == '__main__':
    main()
