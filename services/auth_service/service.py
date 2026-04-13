"""Authentication service logic."""

from __future__ import annotations

from sqlalchemy.orm import Session

from services.auth_service.models import User
from services.auth_service.repository import add_user, get_user_by_email
from shared.security import hash_password, verify_password


def create_admin_user(session: Session, name: str, email: str, password: str) -> User:
    existing_user = get_user_by_email(session, email)
    if existing_user is not None:
        return existing_user

    user = User(
        name=name.strip(),
        email=email.strip().lower(),
        password_hash=hash_password(password),
        is_admin=True,
    )
    return add_user(session, user)


def authenticate_admin(session: Session, email: str, password: str) -> User | None:
    user = get_user_by_email(session, email.strip().lower())
    if user is None or not user.is_admin:
        return None
    if not verify_password(user.password_hash, password):
        return None
    return user
