"""Catalog service logic."""

from __future__ import annotations

from sqlalchemy.orm import Session

from services.catalog_service.models import Book
from services.catalog_service.repository import add_book, get_book_by_id, list_books


def create_book(
    session: Session,
    title: str,
    author: str,
    description: str,
    total_copies: int,
) -> Book:
    normalized_title = title.strip()
    normalized_author = author.strip()
    if not normalized_title:
        raise ValueError("Book title is required.")
    if not normalized_author:
        raise ValueError("Author name is required.")

    normalized_total = max(1, total_copies)
    book = Book(
        title=normalized_title,
        author=normalized_author,
        description=description.strip(),
        total_copies=normalized_total,
        available_copies=normalized_total,
    )
    return add_book(session, book)


def get_catalog_book(session: Session, book_id: int) -> Book | None:
    return get_book_by_id(session, book_id)


def list_catalog_books(session: Session) -> list[Book]:
    return list_books(session)
