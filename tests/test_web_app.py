"""Web application tests."""

from __future__ import annotations

import os
import tempfile
import unittest
from pathlib import Path

from apps.web_app import create_app
from services.auth_service.service import create_admin_user
from services.catalog_service.service import create_book
from shared.database import create_session, create_tables, initialize_database, reset_database
from shared.model_loader import load_models


class WebAppFlowTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.tempdir = tempfile.TemporaryDirectory()
        database_path = Path(self.tempdir.name) / "web-test.db"
        self.original_database_url = os.environ.get("LIBRARY_DATABASE_URL")
        self.original_secret_key = os.environ.get("LIBRARY_SECRET_KEY")

        os.environ["LIBRARY_DATABASE_URL"] = f"sqlite:///{database_path}"
        os.environ["LIBRARY_SECRET_KEY"] = "test-secret-key"

        reset_database()
        initialize_database(os.environ["LIBRARY_DATABASE_URL"])
        create_tables(load_models)

        session = create_session()
        try:
            admin = create_admin_user(
                session,
                name="Admin",
                email="admin@test.local",
                password="admin123",
            )
            book = create_book(
                session,
                title="Refactoring",
                author="Martin Fowler",
                description="Improving the design of existing code.",
                total_copies=2,
            )
            self.admin_email = admin.email
            self.book_id = book.id
        finally:
            session.close()

        self.app = create_app()
        self.client = self.app.test_client()

    def tearDown(self) -> None:
        reset_database()

        if self.original_database_url is None:
            os.environ.pop("LIBRARY_DATABASE_URL", None)
        else:
            os.environ["LIBRARY_DATABASE_URL"] = self.original_database_url

        if self.original_secret_key is None:
            os.environ.pop("LIBRARY_SECRET_KEY", None)
        else:
            os.environ["LIBRARY_SECRET_KEY"] = self.original_secret_key

        self.tempdir.cleanup()

    def login(self) -> None:
        response = self.client.post(
            "/login",
            data={"email": self.admin_email, "password": "admin123"},
            follow_redirects=True,
        )
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Dashboard", response.data)

    def test_login_dashboard_and_issue_return_flow(self) -> None:
        self.login()

        issue_response = self.client.post(
            "/loans",
            data={"borrower_name": "Ana", "book_id": str(self.book_id)},
            follow_redirects=True,
        )
        self.assertEqual(issue_response.status_code, 200)
        self.assertIn(b"Book issued successfully.", issue_response.data)
        self.assertIn(b"Ana", issue_response.data)

        return_response = self.client.post(
            "/loans/1/return",
            follow_redirects=True,
        )
        self.assertEqual(return_response.status_code, 200)
        self.assertIn(b"Book returned successfully.", return_response.data)
        self.assertIn(b"No open loans yet.", return_response.data)
