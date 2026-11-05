# Requisitos: Python 3.9+ y Pandoc 3.x en PATH.
param(
    [ValidateSet('es', 'va', 'ca', 'all')][string]$Lang = 'es',
    [string]$OutDir = 'public/epub'
)

$ErrorActionPreference = 'Stop'
& python (Join-Path $PSScriptRoot 'export-course.py') --format epub --lang $Lang --out-dir $OutDir
if ($LASTEXITCODE -ne 0) { throw 'No se ha podido generar el EPUB.' }
