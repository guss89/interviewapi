import os
from dotenv import load_dotenv

# Cargar las variables de entorno del archivo .env
load_dotenv()

class Settings:
    # Configuración básica de la app
    APP_NAME: str = "Intervie API"
    APP_VERSION: str = "1.0.0"

    # Base de datos
    DB_USER: str = os.getenv("DB_USER")
    DB_PASSWORD: str = os.getenv("DB_PASSWORD")
    DB_HOST: str = os.getenv("DB_HOST", "localhost")
    DB_PORT: str = os.getenv("DB_PORT", "3306")  # Default para MySQL
    DB_NAME: str = os.getenv("DB_NAME")

    SQLALCHEMY_DATABASE_URL: str = (
        f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
    )

    # Seguridad (puedes agregarlo después si haces autenticación)
    SECRET_KEY: str = "Ut_kOosRyUrS4cBGOZBSyPEN7PYRekDoB4DqJBoLsH_GfpNwzslDdzNljOZdv0an"
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60

# Crear una instancia para usar en la app
settings = Settings()