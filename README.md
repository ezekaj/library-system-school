# Library System School

A small library management system built for a school seminar.

## Goal

Build a defensible MVP that can be demonstrated in class, deployed on an Ubuntu virtual machine, and explained with a clean architecture and ERD.

## Planned Architecture

- `apps/web_app`: Flask UI and presentation layer
- `services/auth_service`: admin authentication and user records
- `services/catalog_service`: book catalog management
- `services/circulation_service`: issue and return flows
- `shared/`: shared config, contracts, database helpers, and utility functions

## MVP Features

- Admin login
- View books
- Add books
- Issue books
- Return books
- SQLite persistence
- Seeded demo data
- ERD and seminar materials

## Quick Start

```bash
python3 -m venv .venv
.venv/bin/pip install -r requirements.txt
.venv/bin/python -m scripts.seed_demo
.venv/bin/python -m apps.web_app
```

Open `http://127.0.0.1:5000`.

## Default Admin

- Email: `admin@library.local`
- Password: `admin123`

## Run Tests

```bash
.venv/bin/python -m unittest discover -s tests -v
```

## Seminar Docs

- Architecture overview: `docs/architecture/overview.md`
- Diagrams: `docs/architecture/diagrams.md`
- ERD: `docs/erd/library-system-erd.md`
- Ubuntu VM deployment guide: `docs/seminar/ubuntu-vm-deployment.md`
- Presentation outline: `docs/seminar/presentation-outline.md`
- Speaker notes: `docs/seminar/speaker-notes.md`
