#!/usr/bin/env python3
"""Comprueba la estructura de los tres idiomas y los enlaces de la versión catalana."""

from pathlib import Path
import re
import sys
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / 'src/content/docs'
BASE = '/ApuntsProgramacio/'
LINK = re.compile(r'(?:\]\(|(?:href|src)=["\'])(/ApuntsProgramacio/[^\s)"\']*)')
FENCE = re.compile(r'(?ms)^([ \t]*)(`{3,}|~{3,})[^\n]*\n.*?^\1\2[ \t]*(?:\n|$)')


def files(language):
    folder = DOCS if language == 'es' else DOCS / language
    return {p.relative_to(folder): p for p in folder.rglob('*.md')
            if language != 'es' or p.relative_to(folder).parts[0] not in ('va', 'ca')}


def main():
    languages = {lang: files(lang) for lang in ('es', 'va', 'ca')}
    errors = []
    reference = set(languages['es'])
    for lang, entries in languages.items():
        for name in sorted(reference - set(entries)):
            errors.append(f'{lang}: falta {name}')
        for name in sorted(set(entries) - reference):
            errors.append(f'{lang}: archivo sin equivalente: {name}')
        for name, path in entries.items():
            if str(name) != str(name).lower():
                errors.append(f'{lang}: nombre con mayúsculas: {name}')
            text = path.read_text(encoding='utf-8-sig')
            if '\ufffd' in text or '\r' in path.read_bytes().decode('utf-8-sig'):
                errors.append(f'{lang}: codificación o saltos de línea incorrectos: {name}')

    for name, path in languages['ca'].items():
        text = path.read_text()
        prose = FENCE.sub('', text)
        for match in LINK.finditer(prose):
            route = unquote(urlsplit(match[1]).path)[len(BASE):].rstrip('/')
            target = ROOT / 'public' / route
            if target.is_file():
                continue
            if not route.startswith('ca/'):
                errors.append(f'ca/{name}: enlace fuera del idioma o recurso inexistente: {match[1]}')
                continue
            slug = route[3:]
            candidates = (Path(slug + '.md'), Path(slug) / 'index.md') if slug else (Path('index.md'),)
            if not any(candidate in languages['ca'] for candidate in candidates):
                errors.append(f'ca/{name}: enlace sin destino: {match[1]}')
        # Esta adaptación conserva el código y las salidas de la edición valenciana.
        source = languages['va'].get(name)
        if source:
            original = [m[0] for m in FENCE.finditer(source.read_text(encoding='utf-8-sig'))]
            adapted = [m[0] for m in FENCE.finditer(text)]
            if original != adapted:
                errors.append(f'ca/{name}: el código difiere de la versión valenciana')
            inline = re.compile(r'(?<!`)`([^`\n]+)`(?!`)')
            if inline.findall(source.read_text(encoding='utf-8-sig')) != inline.findall(text):
                errors.append(f'ca/{name}: el código en línea difiere de la versión valenciana')

    if errors:
        print('\n'.join(errors), file=sys.stderr)
        return 1
    print('Estructura ES/VA/CA sincronizada: ' + ', '.join(f'{lang}={len(entries)}' for lang, entries in languages.items()))
    print('Enlaces y recursos CA correctos; bloques de código y salidas conservados.')
    return 0


if __name__ == '__main__':
    sys.exit(main())
