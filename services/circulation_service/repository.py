"""Circulation repository functions."""

from __future__ import annotations

from sqlalchemy import select
from sqlalchemy.orm import Session

from services.circulation_service.models import Loan


def add_loan(session: Session, loan: Loan) -> Loan:
    session.add(loan)
    session.commit()
    session.refresh(loan)
    return loan


def get_loan_by_id(session: Session, loan_id: int) -> Loan | None:
    statement = select(Loan).where(Loan.id == loan_id)
    return session.scalar(statement)


def list_active_loans(session: Session) -> list[Loan]:
    statement = select(Loan).where(Loan.returned_at.is_(None)).order_by(Loan.issued_at.desc())
    return list(session.scalars(statement))


def save_changes(session: Session) -> None:
    session.commit()
