# config/base.py

from pydantic_settings import BaseSettings
from pydantic import Field
from typing import List
from uuid import uuid4
from datetime import datetime


class BaseAppSettings(BaseSettings):
    app_name: str = Field(default="Mi App")
    debug: bool = Field(default=False)
    environment: str = Field(default="development")
    db_url: str = Field(default="sqlite:///default.db")
    tags: List[str] = Field(default_factory=list)
    session_token: str = Field(default_factory=lambda: str(uuid4()))
    started_at: datetime = Field(default_factory=datetime.utcnow)

    class Config:
        env_file_encoding = "utf-8"
