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
_current_database_url: str | None = None


def initialize_database(database_url: str) -> None:
    global _current_database_url, _engine, _session_factory

    if _engine is not None and _current_database_url == database_url:
        return

    if _engine is not None:
        _engine.dispose()

    connect_args = {"check_same_thread": False} if database_url.startswith("sqlite") else {}
    _engine = create_engine(database_url, echo=False, future=True, connect_args=connect_args)
    _session_factory = sessionmaker(bind=_engine, autoflush=False, autocommit=False)
    _current_database_url = database_url


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


def drop_tables(load_models: Callable[[], None]) -> None:
    if _engine is None:
        raise RuntimeError("Database has not been initialized.")
    load_models()
    Base.metadata.drop_all(_engine)


def reset_database() -> None:
    global _current_database_url, _engine, _session_factory

    if _engine is not None:
        _engine.dispose()

    _engine = None
    _session_factory = None
    _current_database_url = None
