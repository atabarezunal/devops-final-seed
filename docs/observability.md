# Observabilidad

La aplicación incorpora mecanismos básicos de observabilidad orientados a facilitar monitoreo, diagnóstico y recolección de métricas durante ejecución local o despliegue en contenedores.

La estrategia implementada se compone de tres elementos principales:

- Health checks
- Métricas Prometheus
- Logs estructurados

---

## Endpoint `/health`

El endpoint `/health` permite verificar rápidamente el estado de disponibilidad de la aplicación.

Ruta:

```text
GET /health
```

Respuesta esperada:

```json
{
  "status": "ok"
}
```

Este endpoint puede ser utilizado por:

- Docker Compose
- Kubernetes
- Load balancers
- Herramientas de monitoreo
- Pipelines CI/CD

El objetivo es permitir validaciones automáticas sobre el estado operativo de la API.

---

## Endpoint `/metrics`

La aplicación expone métricas compatibles con Prometheus mediante el endpoint:

```text
GET /metrics
```

La implementación utiliza la librería `prometheus-client`.

Actualmente se registra un contador de solicitudes HTTP realizadas sobre la API.

Ejemplo de salida:

```text
# HELP http_requests_total Total HTTP Requests
# TYPE http_requests_total counter
http_requests_total{method="GET",endpoint="/tasks"} 12.0
```

Las métricas permiten monitorear:

- Cantidad de requests
- Endpoints más utilizados
- Métodos HTTP utilizados

La información recolectada puede ser consumida posteriormente por Prometheus y visualizada en Grafana.

---

## Integración con Prometheus

La aplicación fue preparada para integrarse con Prometheus mediante scraping periódico del endpoint `/metrics`.

Prometheus realiza solicitudes automáticas hacia:

```text
http://app:5000/metrics
```

Esto permite centralizar métricas de ejecución y generar dashboards de monitoreo.

La configuración de Prometheus y Grafana se encuentra desacoplada del backend y es gestionada desde Docker Compose y archivos de infraestructura.

---

## Provisioning de Grafana

Grafana quedó configurado para arrancar sin intervención manual mediante archivos de provisioning montados desde Docker Compose.

### Datasource

El datasource de Prometheus se carga automáticamente desde:

```text
grafana/provisioning/datasources/datasources.yml
```

Este datasource apunta a:

```text
http://prometheus:9090
```

### Dashboards

La carga automática de dashboards se define en:

```text
grafana/provisioning/dashboards/dashboards.yml
```

Los JSON de dashboards se leen desde:

```text
grafana/dashboards/
```

### Dashboard incluido

Se añadió un dashboard base en:

```text
grafana/dashboards/dashboard_todo.json
```

Este dashboard incluye varias vistas sobre la métrica `app_requests_total` y métricas de salud de Prometheus como `up` y `scrape_duration_seconds`.

### Montaje en Docker Compose

Grafana monta estas rutas en el contenedor:

```text
/etc/grafana/provisioning
/etc/grafana/dashboards
```

Con esto, el datasource y los paneles quedan disponibles al iniciar el stack con `docker compose up --build`.

---

## Logs estructurados

Se implementó un sistema de logs estructurados utilizando el módulo `logging` de Python.

Los logs se serializan en formato JSON para facilitar procesamiento por herramientas de monitoreo y agregación de logs.

Ejemplo:

```json
{
  "level": "INFO",
  "message": "GET /tasks",
  "module": "app",
  "logger": "todo-api"
}
```

Los logs son enviados a `stdout`, lo que permite compatibilidad directa con:

- Docker
- Kubernetes
- Promtail
- Loki
- Grafana
- Sistemas de logging centralizado

---

## Objetivo de la observabilidad implementada

La configuración realizada busca proporcionar una base mínima de monitoreo para ambientes DevOps modernos.

Aunque se trata de una aplicación pequeña, la integración de métricas, health checks y logs estructurados permite aplicar prácticas similares a las utilizadas en entornos productivos reales.