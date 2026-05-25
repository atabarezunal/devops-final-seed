import os
from dotenv import load_dotenv

# Carga variables de entorno desde .env
load_dotenv()


class Config:
    PORT = int(os.environ.get("PORT", 5000))

    DB_PATH = os.environ.get(
        "DB_PATH",
        "tasks.db"
    )

    FLASK_ENV = os.environ.get(
        "FLASK_ENV",
        "development"
    )