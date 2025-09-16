# PokeAPI QA Automation (Behave + Requests)

## Objetivo
Suite de pruebas funcionales y de paginación para PokeAPI, con pruebas negativas, validación de schema, tiempos de respuesta y headers.

## Requisitos
- Python 3.10+
- pip, virtualenv
- VS Code (opcional)

## Setup bash
python -m venv .venv
source .venv/bin/activate #en Windows
pip install -r requirements.txt
cp configs/settings.example.env configs/settings.env

## Ejecutar 

Activar entorno virtual 
# Activa el entorno virtual
.\.venv\Scripts\Activate


behave -f pretty -f json -o reports/behave_report.json 
behave -t @happy_path
behave -f pretty

## structura
features: Feature files y steps
src/api: Cliente HTTP y modelos
src/utils: Validadores, schema, timing y logging
reports: Reportes y evidencia
.github/workflows: CI

## Decisiones
Validación de schema con jsonschema.
Límite por defecto comprobado con 20 resultados.
Retrys con backoff para resiliencia.
Evidencia automática en fallos.

## Limitaciones
429 depende de políticas actuales de PokeAPI.
Algunos headers de seguridad pueden no estar presentes en API pública.
Mejora futura
Reporte HTML.
Cache-Control estricto por entorno.
