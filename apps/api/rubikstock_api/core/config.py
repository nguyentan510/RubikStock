from __future__ import annotations

from functools import lru_cache
from typing import Annotated

from pydantic import Field, field_validator
from pydantic_settings import BaseSettings, NoDecode, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=(".env", "../../.env"),
        env_file_encoding="utf-8",
        extra="ignore",
    )

    app_name: str = "RubikStock API"
    app_env: str = "local"
    app_version: str = "0.1.0"
    log_level: str = "INFO"
    api_v1_prefix: str = "/api/v1"
    database_url: str = "postgresql+psycopg://rubikstock:rubikstock@localhost:5433/rubikstock"
    allowed_origins: Annotated[list[str], NoDecode] = Field(
        default_factory=lambda: [
            "http://localhost:3000",
            "http://127.0.0.1:3000",
        ]
    )
    supabase_url: str = ""
    supabase_anon_key: str = ""
    supabase_service_role_key: str = ""

    @field_validator("allowed_origins", mode="before")
    @classmethod
    def _parse_allowed_origins(cls, value: object) -> list[str]:
        if value is None:
            return []
        if isinstance(value, list):
            return [str(item).strip() for item in value if str(item).strip()]
        if isinstance(value, str):
            return [item.strip() for item in value.split(",") if item.strip()]
        raise TypeError("allowed_origins must be a comma-separated string or list")

    @property
    def is_production(self) -> bool:
        return self.app_env.lower() == "production"


@lru_cache(maxsize=1)
def get_settings() -> Settings:
    return Settings()
