"""Application configuration helpers."""

from __future__ import annotations

import os
from dataclasses import dataclass
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent.parent
DEFAULT_DATABASE_PATH = BASE_DIR / "data" / "library.db"


@dataclass(frozen=True)
class Settings:
    secret_key: str
    database_url: str
    debug: bool


def _read_bool(name: str, default: bool = False) -> bool:
    value = os.getenv(name)
    if value is None:
        return default
    return value.lower() in {"1", "true", "yes", "on"}


def _build_default_database_url() -> str:
    DEFAULT_DATABASE_PATH.parent.mkdir(parents=True, exist_ok=True)
    return f"sqlite:///{DEFAULT_DATABASE_PATH}"


def load_settings() -> Settings:
    return Settings(
        secret_key=os.getenv("LIBRARY_SECRET_KEY", "dev-secret-key"),
        database_url=os.getenv("LIBRARY_DATABASE_URL", _build_default_database_url()),
        debug=_read_bool("LIBRARY_DEBUG"),
    )
