"""Service-level tests."""

from __future__ import annotations

import tempfile
import unittest
from pathlib import Path

from services.auth_service.service import create_admin_user
from services.catalog_service.service import create_book, get_catalog_book
from services.circulation_service.service import issue_book, list_open_loans, return_book
from shared.database import create_session, create_tables, initialize_database, reset_database
from shared.model_loader import load_models


class ServiceFlowTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.tempdir = tempfile.TemporaryDirectory()
        database_path = Path(self.tempdir.name) / "services-test.db"

        reset_database()
        initialize_database(f"sqlite:///{database_path}")
        create_tables(load_models)

        self.session = create_session()
        self.admin = create_admin_user(
            self.session,
            name="Admin",
            email="admin@test.local",
            password="admin123",
        )
        self.book = create_book(
            self.session,
            title="Clean Architecture",
            author="Robert C. Martin",
            description="Architecture and boundaries.",
            total_copies=2,
        )

    def tearDown(self) -> None:
        self.session.close()
        reset_database()
        self.tempdir.cleanup()

    def test_issue_and_return_updates_inventory(self) -> None:
        loan = issue_book(
            self.session,
            book_id=self.book.id,
            borrower_name="Ana",
            issued_by_user_id=self.admin.id,
        )

        updated_book = get_catalog_book(self.session, self.book.id)
        self.assertIsNotNone(updated_book)
        self.assertEqual(updated_book.available_copies, 1)
        self.assertEqual(len(list_open_loans(self.session)), 1)

        returned_loan = return_book(self.session, loan.id)
        updated_book = get_catalog_book(self.session, self.book.id)

        self.assertIsNotNone(returned_loan.returned_at)
        self.assertIsNotNone(updated_book)
        self.assertEqual(updated_book.available_copies, 2)
        self.assertEqual(len(list_open_loans(self.session)), 0)
