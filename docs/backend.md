# Backend

## Arquitectura de la aplicación

La API fue desarrollada en Flask siguiendo una estructura modular simple orientada a facilitar mantenimiento, pruebas y despliegue. Aunque el proyecto corresponde a una aplicación pequeña, se separaron responsabilidades principales para evitar lógica centralizada en un único archivo.

La estructura backend quedó organizada de la siguiente manera:

```text
src/
├── __init__.py
├── app.py
├── config.py
├── database.py
└── logger.py
```

`app.py` contiene la definición de rutas HTTP, validaciones y configuración principal de Flask.

`config.py` centraliza las variables de entorno utilizadas por la aplicación, permitiendo desacoplar configuración del código fuente.

`database.py` encapsula la conexión SQLite y la inicialización de tablas.

`logger.py` implementa logs estructurados en formato JSON para facilitar integración con herramientas de observabilidad y contenedores Docker.

La aplicación utiliza SQLite como base de datos ligera para simplificar el despliegue y reducir dependencias externas.

---

## Endpoints implementados

### GET /

Retorna información general de la API y los endpoints disponibles.

Ejemplo de respuesta:

```json
{
  "name": "To-Do API",
  "version": "1.0.0"
}
```

---

### GET /tasks

Obtiene todas las tareas registradas en la base de datos.

---

### POST /tasks

Crea una nueva tarea.

Body esperado:

```json
{
  "title": "Nueva tarea",
  "description": "Descripción opcional"
}
```

---

### GET /tasks/<id>

Obtiene una tarea específica utilizando su identificador.

---

### PUT /tasks/<id>

Actualiza los datos de una tarea existente.

---

### DELETE /tasks/<id>

Elimina una tarea de la base de datos.

---

### GET /health

Endpoint utilizado para verificar disponibilidad de la aplicación.

---

### GET /metrics

Expone métricas compatibles con Prometheus.

---

## Ejecución local

Se recomienda trabajar dentro de un entorno virtual para evitar conflictos con dependencias globales.

Crear entorno virtual:

```bash
python -m venv venv
```

Activar entorno:

Windows:

```bash
source venv/Scripts/activate
```

Linux/macOS:

```bash
source venv/bin/activate
```

Instalar dependencias:

```bash
pip install -r requirements.txt
pip install -r requirements-dev.txt
```

Ejecutar aplicación:

```bash
python src/app.py
```

La API queda disponible en:

```text
http://localhost:5000
```

---

## Ejecución de pruebas

Las pruebas unitarias fueron implementadas utilizando `pytest`.

Para ejecutarlas:

```bash
pytest
```

Las pruebas cubren operaciones principales de la API:

- Consulta raíz
- Obtención de tareas
- Creación de tareas
- Actualización de tareas
- Eliminación de tareas

---

## Variables de entorno

La configuración se maneja mediante variables de entorno cargadas desde `.env`.

Variables utilizadas:

| Variable | Descripción |
|---|---|
| PORT | Puerto de ejecución |
| DB_PATH | Ruta del archivo SQLite |
| FLASK_ENV | Entorno de ejecución |

Archivo de ejemplo:

```env
PORT=5000
DB_PATH=tasks.db
FLASK_ENV=development
```

---

## Validaciones implementadas

Se agregaron validaciones básicas sobre los datos recibidos por la API para reducir errores y mejorar consistencia.

Entre las validaciones implementadas se encuentran:

- Verificación de existencia del campo `title`
- Validación de tipo string para títulos
- Prevención de títulos vacíos
- Manejo de solicitudes sin body JSON
- Manejo de recursos inexistentes mediante respuestas HTTP 404
- Manejo de errores internos mediante handlers HTTP 500

Estas validaciones permiten responder errores controlados y evitar fallos inesperados dentro de la aplicación.