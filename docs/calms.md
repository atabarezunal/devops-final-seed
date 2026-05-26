# CALMS y Arquitectura de Despliegue

## CALMS

- Culture: colaboración entre desarrollo e infraestructura
- Automation: pipelines y despliegues repetibles
- Lean: minimizar pasos manuales y artefactos innecesarios
- Measurement: métricas, logs y salud de la aplicación
- Sharing: documentación y convenciones visibles para el equipo

## Arquitectura de despliegue

La solución se apoya en una API Flask, una base SQLite persistida por volumen, Prometheus para métricas y Grafana para visualización.

La intención es mantener una arquitectura simple, reproducible y fácil de extender hacia Kubernetes.

## Relación con DevOps

La cultura CALMS se traduce en decisiones concretas del proyecto:

- Culture: el trabajo se separa por responsabilidades para que infraestructura y aplicación evolucionen sin bloquearse.
- Automation: el pipeline valida calidad, seguridad y build de manera automática.
- Lean: se evita sobreingeniería; la base SQLite simplifica el arranque y el volumen preserva datos.
- Measurement: Prometheus recolecta métricas y la API expone `/health` y `/metrics`.
- Sharing: la documentación explica cómo se construye, despliega y valida la solución.

## Flujo de despliegue

1. El código se integra en una rama `feature/*` mediante pull request.
2. El pipeline ejecuta linting, tests, auditoría y build de imagen.
3. Se generan artefactos para revisión y trazabilidad.
4. La imagen y los manifiestos se usan como base para despliegue local o en Kubernetes.

## Coherencia de la arquitectura

- Docker Compose orquesta la API, Prometheus y Grafana en una red interna.
- Prometheus scrapea a la API por su nombre de servicio.
- Kubernetes replica la misma intención con Deployment, Service, ConfigMap, PersistentVolumeClaim e Ingress.
- SQLite se persiste por volumen tanto en Docker Compose como en Kubernetes, manteniendo la misma ruta de datos `/data/tasks.db`.

## Elementos entregados

- Contenerización con `Dockerfile` y `docker-compose.yml`.
- Observabilidad con Prometheus, Grafana y dashboard provisionado automáticamente.
- Automatización CI/CD con GitHub Actions.
- Base de despliegue en Kubernetes para evolución futura.