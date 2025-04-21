# config/settings.py

from config.base import BaseAppSettings


class DevSettings(BaseAppSettings):
    class Config:
        env_file = "config/dev.env"


class ProdSettings(BaseAppSettings):
    class Config:
        env_file = "config/prod.env"


def get_settings():
    from os import getenv
    env = getenv("ENVIRONMENT", "development")

    if env == "production":
        return ProdSettings()
    return DevSettings()


settings = get_settings()
