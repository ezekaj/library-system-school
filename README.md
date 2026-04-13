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
