"""Circulation service models."""

from __future__ import annotations

from datetime import datetime

from sqlalchemy import DateTime, ForeignKey, Integer, String
from sqlalchemy.orm import Mapped, mapped_column

from shared.database import Base
from shared.time import utc_now


class Loan(Base):
    """Book loan record."""

    __tablename__ = "loans"

    id: Mapped[int] = mapped_column(primary_key=True)
    book_id: Mapped[int] = mapped_column(ForeignKey("books.id"), nullable=False)
    borrower_name: Mapped[str] = mapped_column(String(255), nullable=False)
    issued_by_user_id: Mapped[int] = mapped_column(ForeignKey("users.id"), nullable=False)
    issued_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=utc_now, nullable=False)
    returned_at: Mapped[datetime | None] = mapped_column(DateTime(timezone=True), nullable=True)
