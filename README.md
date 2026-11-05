# ☕ Apuntes Programación Java — DAM/DAW

Curso completo de **Programación en Java** para DAM/DAW. Material en castellano, valenciano y catalán con **16 unidades** (15 estándar + 1 extra de APIs), **76 boletines de ejercicios** por idioma y proyecto final.

## Estructura del curso (UD1–UD16)
| # | Unidad | RA |
|---|---|---|
| 01 | Pensamiento computacional (introductoria) | RA1 |
| 02 | Introducción a Java y el entorno de trabajo | RA1 |
| 03 | Variables, tipos y operadores (incluye consola) | RA2 |
| 04 | Estructuras de control y excepciones básicas | RA3 |
| 05 | Funciones y métodos | RA2 |
| 06 | Arrays | RA6 |
| 07 | Algorítmica I: Fundamentos | RA2, RA6 |
| 08 | Algorítmica II: Técnicas avanzadas y modularidad | RA2, RA6 |
| 09 | POO: Clases y objetos | RA2, RA4 |
| 10 | Visibilidad, encapsulación y static | RA4 |
| 11 | Herencia, polimorfismo e interfaces | RA4, RA7 |
| 12 | Colecciones, genéricos y mapas | RA6 |
| 13 | Programación funcional (Streams y Lambdas) | RA6, RA7 |
| 14 | Ficheros y expresiones regulares (Regex) | RA5, RA6 |
| 15 | Persistencia de datos: JDBC e introducción a ORM | RA9 |
| 16 | Servir y consumir APIs con Web (extra, no evaluable) | RA5 |

Cada unidad tiene 9 puntos de teoría (10 en U03, U08 y U15) y 5 boletines (inicial → inicial-resuelto → avanzado → avanzado-resuelto → extras). Idiomas: castellano (raíz), valenciano (`/va/`) y catalán (`/ca/`).

🌐 **Web del curso:** [sergarb1.github.io/ApuntesProgramacion](https://sergarb1.github.io/ApuntesProgramacion/)

**CC BY-SA 4.0** — *Sergi Garcia Barea*

## Idiomas y exportaciones

La edición catalana usa catalán central estándar y mantiene la estructura de las otras ediciones: 16 unidades y 76 boletines. Sus 240 documentos están en `src/content/docs/ca/`; las tres opciones aparecen en el selector de idioma. Se comparten la portada `portada_val.png` y los ejemplos de código, y los diagramas adaptados al catalán llevan el sufijo `-ca`.

```bash
npm run check:locales  # Estructura ES/VA/CA, enlaces CA y conservación del código
npm run build         # Web completa y búsqueda por idioma
npm run pdf:ca        # PDF catalán desde la web publicada
npm run pdf:local:ca  # PDF catalán desde el servidor local
npm run epub:ca       # EPUB catalán
npm run epub:all      # EPUB de los tres idiomas
npm run docx:ca       # DOCX catalanes, una unidad o boletín por archivo
npm run docx          # DOCX de los tres idiomas
```

Las exportaciones EPUB y DOCX requieren Python 3.9+ y Pandoc 3.x en `PATH`. Para los SVG de los DOCX también se necesita `rsvg-convert` o el paquete Python `cairosvg`. Los scripts de PowerShell siguen disponibles y llaman al mismo exportador; por ejemplo, `powershell -File scripts/generate-docx.ps1 -Lang ca`.

El exportador descubre las unidades actuales, incluye sus índices y capítulos y conserva el orden de los boletines. Las salidas catalanas son `public/pdf/ApuntesProgramacion-ca.pdf`, `public/epub/ApuntesProgramacion-ca.epub` y `docx/ca/`.
