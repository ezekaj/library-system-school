"""Seed the application with a default admin and sample books."""

from __future__ import annotations

from shared.config import load_settings
from shared.database import create_session, create_tables, initialize_database
from shared.model_loader import load_models
from services.auth_service.service import create_admin_user
from services.catalog_service.service import create_book, list_catalog_books


DEFAULT_ADMIN = {
    "name": "Library Admin",
    "email": "admin@library.local",
    "password": "admin123",
}

SAMPLE_BOOKS = [
    {
        "title": "Clean Code",
        "author": "Robert C. Martin",
        "description": "A practical reference on readable code and maintainable software design.",
        "total_copies": 5,
    },
    {
        "title": "The Pragmatic Programmer",
        "author": "Andrew Hunt and David Thomas",
        "description": "Classic engineering habits for iterative, disciplined software work.",
        "total_copies": 4,
    },
    {
        "title": "Designing Data-Intensive Applications",
        "author": "Martin Kleppmann",
        "description": "System design patterns for data models, reliability, and scalability.",
        "total_copies": 3,
    },
]


def seed_demo_data() -> None:
    settings = load_settings()
    initialize_database(settings.database_url)
    create_tables(load_models)

    session = create_session()
    try:
        create_admin_user(session, **DEFAULT_ADMIN)

        if not list_catalog_books(session):
            for book in SAMPLE_BOOKS:
                create_book(session, **book)
    finally:
        session.close()


if __name__ == "__main__":
    seed_demo_data()
    print("Demo data seeded successfully.")
