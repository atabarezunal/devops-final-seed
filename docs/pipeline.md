# Automatización (CI/CD)

Esta sección documenta el flujo de integración y entrega continua del proyecto.

## Objetivo

Definir un pipeline que valide calidad, seguridad y empaquetado antes de producir artefactos listos para revisión o despliegue.

## Flujo implementado

El workflow [`ci-cd.yml`](../.github/workflows/ci-cd.yml) ejecuta las siguientes fases:

1. Instalación de dependencias de producción y desarrollo.
2. Linting con `flake8` sobre `src/` y `tests/`.
3. Ejecución de `pytest` con reporte de cobertura.
4. Auditoría de seguridad con `pip-audit`.
5. Construcción de la imagen Docker con tag basado en `github.sha`.
6. Versionado adicional con `latest` para la última revisión exitosa del flujo.
7. Publicación de artefactos de build para trazabilidad.

## Artefactos generados

- `coverage.xml`
- `pip-audit-report.json`
- `todo-api-<sha>.tar`

## Disparadores

- `push` a `main`
- `push` a `feature/**`
- `pull_request` hacia `main`

## Criterio DevOps

El pipeline está diseñado para fallar rápido si hay problemas de estilo, tests o seguridad, reduciendo el costo de integración y evitando que artefactos inconsistentes avancen a etapas posteriores.