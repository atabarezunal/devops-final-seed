# Seguridad

La aplicación incorpora controles básicos de seguridad y calidad enfocados en reducir errores comunes de desarrollo y facilitar integración con pipelines DevOps.

La estrategia implementada incluye validación de código, auditoría de dependencias y manejo seguro de configuración mediante variables de entorno.

---

## Linting y calidad de código

Se utilizó `flake8` como herramienta de análisis estático para validar cumplimiento de convenciones PEP8 y detectar problemas comunes de calidad.

Configuración utilizada:

```text
.flake8
```

Ejecución:

```bash
flake8 src tests
```

El análisis permite detectar:

- Errores de formato
- Imports incorrectos
- Espacios innecesarios
- Líneas inválidas
- Problemas de estilo

La validación mediante linting también fue pensada para integrarse posteriormente al pipeline CI/CD.

---

## Auditoría de dependencias

Se implementó análisis de vulnerabilidades utilizando herramientas especializadas para dependencias Python.

Herramientas utilizadas:

- pip-audit
- safety

Ejecución:

```bash
pip-audit
```

```bash
safety check
```

La auditoría permite identificar paquetes con vulnerabilidades conocidas reportadas públicamente mediante CVEs.

Durante el desarrollo se actualizaron dependencias principales a versiones más recientes y estables para reducir riesgos asociados a librerías vulnerables.

---

## Variables de entorno

La configuración de la aplicación fue desacoplada del código fuente mediante variables de entorno.

Archivo de ejemplo:

```env
PORT=5000
DB_PATH=tasks.db
FLASK_ENV=development
```

Esto evita hardcodear configuraciones sensibles directamente en la aplicación y facilita despliegue en distintos entornos.

El archivo `.env` fue agregado al `.gitignore` para evitar exposición accidental de información local.

---

## Buenas prácticas implementadas

Se aplicaron prácticas básicas orientadas a mejorar estabilidad y seguridad general de la API.

Entre ellas:

- Separación de configuración y código
- Validación de datos recibidos
- Manejo controlado de errores HTTP
- Uso de entorno virtual para aislamiento de dependencias
- Exclusión de archivos sensibles mediante `.gitignore`
- Logs estructurados para trazabilidad
- Validación automática mediante pruebas unitarias

También se incorporaron handlers para respuestas HTTP 404 y 500, permitiendo reducir exposición de errores internos no controlados.

---

## Seguridad en el flujo DevOps

La configuración implementada fue diseñada para integrarse posteriormente con GitHub Actions dentro del pipeline CI/CD.

Las herramientas de linting y auditoría podrán ejecutarse automáticamente en cada push o pull request para validar calidad y seguridad antes de despliegues o builds Docker.

Esto permite incorporar controles automáticos tempranos dentro del ciclo de desarrollo.