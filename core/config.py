from pydantic import BaseSettings
from typing import Optional
from functools import lru_cache

class Settings(BaseSettings):
    API_V1_STR: str ="/api/v1"
    PROJECT_NAME: str="Sitios en minca"

    POSTGRES_SERVER: srt="localhost"
    POSTGRES_USER: srt="fastapi"
    POSTGRES_PASSWORD: srt="123123"
    POSTGRES_BD: srt="minca"
    SQLALCHEMY_DATABASE_URI: Optional[str] = f"postgresql://{POSTGRES_USER}:{POSTGRES:POSTGRES_PASSWORD}@{POSTGRES_SERVER}/{POSTGRES_BD}" #cadena de conexion

    class Config:
        case_sensitive = True

    @lru_cache
    def get_settings():
        return Settings()

    settings = get_settings() 