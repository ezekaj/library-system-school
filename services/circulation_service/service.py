"""Circulation service logic."""

from __future__ import annotations

from sqlalchemy.orm import Session

from services.catalog_service.repository import get_book_by_id
from services.circulation_service.models import Loan
from services.circulation_service.repository import add_loan, get_loan_by_id, list_active_loans, save_changes
from shared.time import utc_now


def issue_book(session: Session, book_id: int, borrower_name: str, issued_by_user_id: int) -> Loan:
    normalized_borrower = borrower_name.strip()
    if not normalized_borrower:
        raise ValueError("Borrower name is required.")

    book = get_book_by_id(session, book_id)
    if book is None:
        raise ValueError("Selected book does not exist.")
    if book.available_copies < 1:
        raise ValueError("No copies are available for this book.")

    loan = Loan(
        book_id=book.id,
        borrower_name=normalized_borrower,
        issued_by_user_id=issued_by_user_id,
    )
    book.available_copies -= 1
    return add_loan(session, loan)


def return_book(session: Session, loan_id: int) -> Loan:
    loan = get_loan_by_id(session, loan_id)
    if loan is None:
        raise ValueError("Selected loan does not exist.")
    if loan.returned_at is not None:
        raise ValueError("This book has already been returned.")

    book = get_book_by_id(session, loan.book_id)
    if book is None:
        raise ValueError("Book record is missing.")

    loan.returned_at = utc_now()
    book.available_copies += 1
    save_changes(session)
    return loan


def list_open_loans(session: Session) -> list[Loan]:
    return list_active_loans(session)
