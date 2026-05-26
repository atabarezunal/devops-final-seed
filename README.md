# To-Do API — Semilla para Trabajo Final DevOps

API REST básica de gestión de tareas. **Este es el punto de partida** — su trabajo es construir todo el ecosistema DevOps alrededor.

## Endpoints

| Método | Ruta | Descripción |
|--------|------|-------------|
| GET | `/` | Info de la API |
| GET | `/tasks` | Listar todas las tareas |
| POST | `/tasks` | Crear tarea (`{"title": "...", "description": "..."}`) |
| GET | `/tasks/<id>` | Obtener una tarea |
| PUT | `/tasks/<id>` | Actualizar tarea |
| DELETE | `/tasks/<id>` | Eliminar tarea |

## Ejecutar

```bash
pip install -r requirements.txt
python src/app.py
```

La API corre en `http://localhost:5000`.

## Qué falta (su trabajo)

TODO lo relacionado con DevOps. Partiendo de esta app, deben implementar:

1. **Tests unitarios** — Mínimo 5, en carpeta `tests/`
2. **Contenerización (Docker)** — `Dockerfile`, `docker-compose.yml` y volúmenes persistentes
3. **Automatización (CI/CD)** — `.github/workflows/ci-cd.yml` con linting, tests, auditoría, build y artefactos
4. **Configuración de Observabilidad** — `prometheus.yml`, `/health`, `/metrics`, Prometheus y Grafana
5. **Seguridad** — Auditoría de dependencias, linting
6. **Kubernetes (Bonus)** — Manifests en `k8s/`
7. **Estrategia y Documentación DevOps** — `docs/` con pipeline, branching, CALMS y arquitectura de despliegue
8. **Artefactos** — Imagen versionada, reportes de build

Lean el documento del trabajo final para los detalles completos de cada requisito.

## Stack

- **Lenguaje:** Python 3.11
- **Framework:** Flask
- **Base de datos:** SQLite (ya incluida, no necesita instalación)
- **Dependencias:** Ver `requirements.txt`

---

*DevOps & Automatización — UNAL Sede Manizales — 2026-1*

---

## Documentación

La documentación técnica del proyecto se encuentra en la carpeta `docs/`.

- [Backend](docs/backend.md)
- [Configuración de Observabilidad](docs/observability.md)
- [Seguridad](docs/security.md)
- [Automatización CI/CD](docs/pipeline.md)
- [Estrategia de Branching](docs/branching.md)
- [CALMS y Arquitectura](docs/calms.md)

---

