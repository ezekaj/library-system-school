# Presentation Outline

This outline is designed for a short seminar presentation of around 6 to 8 minutes.

## Slide 1: Title

**Library Management System Using Flask, SQLite, and Ubuntu VM**

Talking points:
- introduce the project goal
- explain that the system was built as a small modular web application
- mention the deployment target: Ubuntu inside VirtualBox

## Slide 2: Problem Statement

Talking points:
- libraries need a simple way to track books and loans
- manual tracking is slow and error-prone
- the goal was to create a minimal digital system for administration

## Slide 3: Technologies Used

Talking points:
- `Python` for implementation
- `Flask` for the web application
- `SQLite` for persistence
- `Jinja` for templates
- `VirtualBox` and `Ubuntu` for deployment

## Slide 4: Modular Service Structure

Talking points:
- `auth_service` handles admin login
- `catalog_service` handles books
- `circulation_service` handles issue and return flows
- `web_app` provides the user interface
- all modules run in one Flask deployment, which keeps the project simple to demonstrate

## Slide 5: System Architecture

Talking points:
- browser sends requests to the Flask app
- the Flask app delegates logic to small service modules
- each service reads or writes the SQLite database

Reference:
- use `docs/architecture/diagrams.md`

## Slide 6: Database Design

Talking points:
- `users` stores admins
- `books` stores title, author, and inventory
- `loans` stores issued and returned books

Reference:
- use `docs/erd/library-system-erd.md`

## Slide 7: Main Features

Talking points:
- admin login
- add books
- view all books
- issue a book
- return a book

## Slide 8: Deployment Steps

Talking points:
- create Ubuntu VM
- install Python and git
- clone the repository
- create virtual environment
- install requirements
- seed demo data
- run the application

Reference:
- use `docs/seminar/ubuntu-vm-deployment.md`

## Slide 9: Demonstration

Talking points:
- log in as admin
- show the books table
- add a new book
- issue one book to a borrower
- return the same book and show the updated inventory

## Slide 10: Problems and Fixes

Talking points:
- missing Python packages before dependency installation
- virtual environment setup on Ubuntu
- incorrect static asset endpoint during development
- keeping the seed script runnable from the command line

## Slide 11: Conclusion

Talking points:
- the system works end to end
- the architecture is modular and easy to explain
- the application is simple enough to deploy inside a VM
- future improvements could include student accounts, search, and overdue tracking
