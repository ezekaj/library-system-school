# Slide 1: Title

## Library Management System
### Using Flask, SQLite, and Ubuntu VM

**School Seminar Presentation**

---

# Slide 2: Problem Statement

## The Problem

- Manual book tracking is slow and error-prone
- Libraries need a simple way to manage books and loans
- Existing systems are often too complex for small libraries

**Goal:** Create a minimal, practical digital system for library administration

---

# Slide 3: Technologies Used

## Tech Stack

| Layer | Technology |
|-------|------------|
| **Language** | Python 3 |
| **Framework** | Flask |
| **Templates** | Jinja2 |
| **Database** | SQLite |
| **Deployment** | VirtualBox + Ubuntu |

---

# Slide 4: Modular Service Structure

## Modular Architecture (Not Microservices)

```
├── auth_service/          # Admin login & authentication
├── catalog_service/       # Book management
├── circulation_service/   # Issue & return flows
└── web_app/               # UI & request handling
```

**Key Point:** All modules run in **one Flask deployment** — a modular monolith, not distributed microservices. This keeps the project simple and practical for demonstration.

---

# Slide 5: System Architecture

```
┌─────────────┐
│   Browser   │
└──────┬──────┘
       │
       ▼
┌─────────────────────────┐
│    Flask Web App        │
│  (Thin request layer)   │
└───┬──────┬──────┬───────┘
    │      │      │
    ▼      ▼      ▼
┌──────┐┌─────┐┌────────────┐
│ Auth ││Catalog││Circulation │
│Service││Service││ Service    │
└──┬───┘└──┬──┘└─────┬──────┘
   │       │         │
   └───────┴─────────┘
           │
           ▼
    ┌─────────────┐
    │   SQLite    │
    │  Database   │
    └─────────────┘
```

---

# Slide 6: Database Design

## Three Core Tables

### `users`
- Admin accounts for system access

### `books`
- Title, author, ISBN, total copies, available copies

### `loans`
- Tracks issued and returned books
- Links borrowers to books
- Records issue and return dates

```
users ──┐
        │
books ──┼── loans
        │
        └── (relationships via foreign keys)
```

*See `docs/erd/library-system-erd.md` for full ERD*

---

# Slide 7: Main Features

## What the System Does

✓ **Admin Login** — Secure authentication

✓ **Add Books** — Expand the catalog

✓ **View All Books** — Browse with availability status

✓ **Issue a Book** — Assign to a borrower, auto-decrement inventory

✓ **Return a Book** — Restore availability, update loan status

---

# Slide 8: Deployment

## Ubuntu VM Deployment Steps

```bash
# 1. Clone the repository
git clone <repo-url>

# 2. Set up virtual environment
python3 -m venv .venv
source .venv/bin/activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Seed demo data
python scripts/seed_data.py

# 5. Run the application
flask run --host=0.0.0.0
```

**One-step bootstrap:** `scripts/bootstrap_ubuntu.sh`

---

# Slide 9: Demonstration

## Live Demo

**Screen recordings captured from Ubuntu VM:**

### Video 1: Authentication & Catalog
- Admin login flow
- Viewing books table
- Adding a new book

### Video 2: Circulation
- Issuing a book to a borrower
- Returning the book
- Showing updated inventory

> **Insert screen recordings here during presentation**
> 
> File: `Screen Recording 2026-04-13 at 12.40.57.mov`
> File: `Screen Recording 2026-04-13 at 12.42.34.mov`

---

# Slide 10: Problems & Fixes

## Challenges Encountered

| Problem | Fix |
|---------|-----|
| Missing Python packages | Installed dependencies via `requirements.txt` |
| Virtual environment setup on Ubuntu | Used `python3-venv` package |
| Incorrect static asset endpoint | Fixed Flask routing for CSS/JS files |
| Seed script usability | Made it runnable standalone from CLI |

---

# Slide 11: Conclusion

## Summary

✓ System works end-to-end

✓ Modular architecture, easy to explain and extend

✓ Simple enough to deploy inside a VM

## Future Improvements

- Student accounts and user roles
- Search and filtering
- Overdue tracking and notifications
- Email reminders

**Thank you! Questions?**
