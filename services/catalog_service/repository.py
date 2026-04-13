"""Catalog repository functions."""

from __future__ import annotations

from sqlalchemy import select
from sqlalchemy.orm import Session

from services.catalog_service.models import Book


def list_books(session: Session) -> list[Book]:
    statement = select(Book).order_by(Book.title.asc())
    return list(session.scalars(statement))


def get_book_by_id(session: Session, book_id: int) -> Book | None:
    statement = select(Book).where(Book.id == book_id)
    return session.scalar(statement)


def add_book(session: Session, book: Book) -> Book:
    session.add(book)
    session.commit()
    session.refresh(book)
    return book
