"""Database engine and session management."""

from __future__ import annotations

from typing import Callable

from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, Session, sessionmaker


class Base(DeclarativeBase):
    """Base class for ORM models."""


SessionFactory = sessionmaker[Session]

_engine = None
_session_factory: SessionFactory | None = None


def initialize_database(database_url: str) -> None:
    global _engine, _session_factory

    if _engine is None:
        connect_args = {"check_same_thread": False} if database_url.startswith("sqlite") else {}
        _engine = create_engine(database_url, echo=False, future=True, connect_args=connect_args)
        _session_factory = sessionmaker(bind=_engine, autoflush=False, autocommit=False)


def get_session_factory() -> SessionFactory:
    if _session_factory is None:
        raise RuntimeError("Database has not been initialized.")
    return _session_factory


def create_session() -> Session:
    return get_session_factory()()


def create_tables(load_models: Callable[[], None]) -> None:
    if _engine is None:
        raise RuntimeError("Database has not been initialized.")
    load_models()
    Base.metadata.create_all(_engine)
