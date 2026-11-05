# Genera un DOCX por unidad y por boletín en docx/es, docx/va y docx/ca.
# Requisitos: Python 3.9+, Pandoc 3.x y rsvg-convert o Python con cairosvg para los SVG.
param(
    [string]$Root = (Split-Path -Parent $PSScriptRoot),
    [ValidateSet('es', 'va', 'ca', 'all')][string]$Lang = 'all'
)

$ErrorActionPreference = 'Stop'
& python (Join-Path $PSScriptRoot 'export-course.py') --format docx --lang $Lang --root $Root
if ($LASTEXITCODE -ne 0) { throw 'No se han podido generar los DOCX.' }
