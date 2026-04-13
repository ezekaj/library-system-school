# Architecture Overview

## Design Goal

Keep the system small enough to finish for school, but structured enough to justify a microservice-inspired modular design.

## Service Boundaries

### `apps/web_app`

- Renders HTML pages with Flask and Jinja
- Handles form submissions from the browser
- Calls service-layer functions instead of placing business logic in routes

### `services/auth_service`

- Manages admin users
- Handles password hashing and login verification
- Owns authentication-related queries

### `services/catalog_service`

- Manages book records
- Creates, lists, and validates books
- Owns catalog-related queries

### `services/circulation_service`

- Handles issue and return workflows
- Tracks copy availability
- Enforces basic circulation rules

### `shared/`

- Shared configuration
- Database session helpers
- Simple contracts and validation helpers
- Reusable utility functions

## Why This Structure Fits The Seminar

- The project remains understandable during a short presentation.
- Each module has one clear responsibility.
- The architecture can be explained as separate service modules even though they run inside one repository and one deployable Flask app.
- It supports the class discussion around modularity, maintainability, and deployment.

## Planned Runtime Model

- One repository
- One Flask-based web application
- Service modules separated by responsibility
- SQLite as the local database
- Ubuntu VM as the deployment target

## Data Ownership

- Auth service: `users`
- Catalog service: `books`
- Circulation service: `copies`, `loans`

## Initial Feature Flow

1. Admin logs in.
2. Web app loads dashboard data from service functions.
3. Catalog service returns available books.
4. Circulation service issues or returns a selected book.
5. SQLite persists the result for demonstration.
