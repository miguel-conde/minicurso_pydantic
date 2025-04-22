# config_2/settings.py

from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import Field
from os import getenv
from config_2.base import DatabaseSettings, DirectorySettings, EmailSettings


class BaseAppSettings(BaseSettings):
    environment: str = Field(default="development", alias="ENVIRONMENT")
    
    # Las secciones ya se inicializan con sus propias clases cargando 
    # config_2/prod.env
    database: DatabaseSettings = DatabaseSettings()
    directories: DirectorySettings = DirectorySettings()
    emails: EmailSettings = EmailSettings()

    model_config = SettingsConfigDict(env_file_encoding="utf-8", 
                                      extra="allow")


class DevSettings(BaseAppSettings):
    model_config = SettingsConfigDict(env_file="config_2/dev.env", 
                                      extra="allow")


class ProdSettings(BaseAppSettings):
    model_config = SettingsConfigDict(env_file="config_2/prod.env", 
                                      extra="allow")


def get_settings():
    env = getenv("ENVIRONMENT", "development")
    if env == "production":
        return ProdSettings()
    return DevSettings()
