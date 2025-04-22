# config_2/base.py

from pydantic_settings import BaseSettings
from pydantic import Field, EmailStr, PostgresDsn
from pathlib import Path


class DatabaseSettings(BaseSettings):
    url: PostgresDsn = Field(..., alias="DATABASE_URL")
    pool_size: int = Field(default=10, alias="DATABASE_POOL_SIZE")
    user: str = Field(..., alias="DATABASE_USER")
    password: str = Field(..., alias="DATABASE_PASSWORD")

    model_config = {"env_file": "config_2/prod.env", "extra": "allow"}


class DirectorySettings(BaseSettings):
    base_dir: Path = Field(..., alias="DATA_DIR")
    raw_dir: Path = Field(..., alias="RAW_DIR")
    clean_dir: Path = Field(..., alias="CLEAN_DIR")

    model_config = {"env_file": "config_2/prod.env", "extra": "allow"}


class EmailSettings(BaseSettings):
    contact_email: EmailStr = Field(..., alias="CONTACT_EMAIL")
    support_email: EmailStr = Field(..., alias="SUPPORT_EMAIL")

    model_config = {"env_file": "config_2/prod.env", "extra": "allow"}

