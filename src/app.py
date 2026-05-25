from flask import Flask, request, jsonify
from prometheus_client import Counter, generate_latest
from src.config import Config
from src.database import get_db, init_db
from src.logger import logger

app = Flask(__name__)

# =========================
# Inicializar base de datos
# =========================
init_db()

# =========================
# Métricas Prometheus
# =========================
REQUEST_COUNT = Counter(
    "app_requests_total",
    "Total HTTP requests"
)


@app.before_request
def before_request():
    REQUEST_COUNT.inc()


# =========================
# Rutas principales
# =========================
@app.route("/", methods=["GET"])
def index():
    logger.info("GET /")

    return jsonify({
        "name": "To-Do API",
        "version": "1.0.0",
        "endpoints": [
            "/tasks",
            "/health",
            "/metrics"
        ]
    })


# =========================
# Healthcheck
# =========================
@app.route("/health", methods=["GET"])
def health():
    return jsonify({
        "status": "ok"
    })


# =========================
# Metrics
# =========================
@app.route("/metrics", methods=["GET"])
def metrics():
    return generate_latest(), 200, {
        "Content-Type": "text/plain"
    }


# =========================
# Obtener todas las tareas
# =========================
@app.route("/tasks", methods=["GET"])
def list_tasks():
    logger.info("GET /tasks")

    conn = get_db()

    tasks = conn.execute(
        "SELECT * FROM tasks ORDER BY created_at DESC"
    ).fetchall()

    conn.close()

    return jsonify([dict(task) for task in tasks])


# =========================
# Crear tarea
# =========================
@app.route("/tasks", methods=["POST"])
def create_task():
    logger.info("POST /tasks")

    data = request.get_json()

    if not data:
        return jsonify({
            "error": "No se enviaron datos"
        }), 400

    title = data.get("title")
    description = data.get("description", "")

    # Validaciones
    if title is None:
        return jsonify({
            "error": "El campo 'title' es obligatorio"
        }), 400

    if not isinstance(title, str):
        return jsonify({
            "error": "El título debe ser un string"
        }), 400

    if not title.strip():
        return jsonify({
            "error": "El título no puede estar vacío"
        }), 400

    conn = get_db()

    cursor = conn.execute(
        """
        INSERT INTO tasks (title, description)
        VALUES (?, ?)
        """,
        (title.strip(), description)
    )

    task_id = cursor.lastrowid

    conn.commit()

    task = conn.execute(
        "SELECT * FROM tasks WHERE id = ?",
        (task_id,)
    ).fetchone()

    conn.close()

    return jsonify(dict(task)), 201


# =========================
# Obtener tarea por ID
# =========================
@app.route("/tasks/<int:task_id>", methods=["GET"])
def get_task(task_id):
    logger.info(f"GET /tasks/{task_id}")

    conn = get_db()

    task = conn.execute(
        "SELECT * FROM tasks WHERE id = ?",
        (task_id,)
    ).fetchone()

    conn.close()

    if task is None:
        return jsonify({
            "error": "Tarea no encontrada"
        }), 404

    return jsonify(dict(task))


# =========================
# Actualizar tarea
# =========================
@app.route("/tasks/<int:task_id>", methods=["PUT"])
def update_task(task_id):
    logger.info(f"PUT /tasks/{task_id}")

    data = request.get_json()

    if not data:
        return jsonify({
            "error": "No se enviaron datos"
        }), 400

    conn = get_db()

    task = conn.execute(
        "SELECT * FROM tasks WHERE id = ?",
        (task_id,)
    ).fetchone()

    if task is None:
        conn.close()

        return jsonify({
            "error": "Tarea no encontrada"
        }), 404

    title = data.get("title", task["title"])
    description = data.get(
        "description",
        task["description"]
    )
    completed = data.get(
        "completed",
        task["completed"]
    )

    # Validación title
    if not isinstance(title, str):
        conn.close()

        return jsonify({
            "error": "El título debe ser un string"
        }), 400

    if not title.strip():
        conn.close()

        return jsonify({
            "error": "El título no puede estar vacío"
        }), 400

    conn.execute(
        """
        UPDATE tasks
        SET title = ?, description = ?, completed = ?
        WHERE id = ?
        """,
        (
            title.strip(),
            description,
            completed,
            task_id
        )
    )

    conn.commit()

    updated_task = conn.execute(
        "SELECT * FROM tasks WHERE id = ?",
        (task_id,)
    ).fetchone()

    conn.close()

    return jsonify(dict(updated_task))


# =========================
# Eliminar tarea
# =========================
@app.route("/tasks/<int:task_id>", methods=["DELETE"])
def delete_task(task_id):
    logger.info(f"DELETE /tasks/{task_id}")

    conn = get_db()

    task = conn.execute(
        "SELECT * FROM tasks WHERE id = ?",
        (task_id,)
    ).fetchone()

    if task is None:
        conn.close()

        return jsonify({
            "error": "Tarea no encontrada"
        }), 404

    conn.execute(
        "DELETE FROM tasks WHERE id = ?",
        (task_id,)
    )

    conn.commit()
    conn.close()

    return jsonify({
        "message": "Tarea eliminada"
    }), 200


# =========================
# Error handlers
# =========================
@app.errorhandler(404)
def not_found(error):
    return jsonify({
        "error": "Recurso no encontrado"
    }), 404


@app.errorhandler(500)
def internal_error(error):
    return jsonify({
        "error": "Error interno del servidor"
    }), 500


# =========================
# Main
# =========================
if __name__ == "__main__":
    logger.info(
        f"Starting To-Do API on port {Config.PORT}"
    )

    app.run(
        host="0.0.0.0",
        port=Config.PORT
    )