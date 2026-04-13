"""Authentication repository functions."""

from __future__ import annotations

from sqlalchemy import select
from sqlalchemy.orm import Session

from services.auth_service.models import User


def get_user_by_email(session: Session, email: str) -> User | None:
    statement = select(User).where(User.email == email)
    return session.scalar(statement)


def get_user_by_id(session: Session, user_id: int) -> User | None:
    statement = select(User).where(User.id == user_id)
    return session.scalar(statement)


def add_user(session: Session, user: User) -> User:
    session.add(user)
    session.commit()
    session.refresh(user)
    return user
