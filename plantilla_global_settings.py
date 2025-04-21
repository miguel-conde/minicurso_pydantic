# global_settings.py

from pydantic import Field
from pydantic_settings import BaseSettings
from typing import List
from uuid import uuid4
from datetime import datetime


# ⚙️ Clase de configuración principal
class Settings(BaseSettings):
    app_name: str = Field(default="Mi Aplicación",
                          description="Nombre de la aplicación")
    debug: bool = Field(default=False, description="Modo debug activado")
    environment: str = Field(default="development",
                             description="Entorno de ejecución")

    # Base de datos
    db_host: str = Field(default="localhost", alias="DB_HOST")
    db_port: int = Field(default=5432, alias="DB_PORT")
    db_user: str = Field(default="admin", alias="DB_USER")
    db_password: str = Field(default="secret", alias="DB_PASSWORD")
    db_name: str = Field(default="app_db", alias="DB_NAME")

    # Otros patrones útiles
    default_tags: List[str] = Field(default_factory=list)
    session_token: str = Field(default_factory=lambda: str(uuid4()))
    started_at: datetime = Field(default_factory=datetime.utcnow)

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


# 🧪 Instancia global reutilizable
settings = Settings()
