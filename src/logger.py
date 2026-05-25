import logging
import json


class JsonFormatter(logging.Formatter):

    def format(self, record):
        log_record = {
            "level": record.levelname,
            "message": record.getMessage(),
            "module": record.module,
            "logger": record.name
        }

        return json.dumps(log_record)


# Crea logger
logger = logging.getLogger("todo-api")

# Nivel de logs
logger.setLevel(logging.INFO)

# Handler para consola
handler = logging.StreamHandler()

# Formato JSON
handler.setFormatter(JsonFormatter())

# Evita duplicar handlers
if not logger.handlers:
    logger.addHandler(handler)
