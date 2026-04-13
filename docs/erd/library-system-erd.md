# Library System ERD

This ERD is generated from the current SQLAlchemy models.

```mermaid
erDiagram
    users {
        int id PK
        string name required
        string email required
        string password_hash required
        boolean is_admin required
        datetime created_at required
    }
    books {
        int id PK
        string title required
        string author required
        text description required
        int total_copies required
        int available_copies required
        datetime created_at required
    }
    loans {
        int id PK
        int book_id FK required
        string borrower_name required
        int issued_by_user_id FK required
        datetime issued_at required
        datetime returned_at
    }

    users ||--o{ loans : issues
    books ||--o{ loans : contains
```

## Notes

- `users` stores admin accounts.
- `books` stores catalog metadata and available inventory.
- `loans` stores each issue and return transaction.
