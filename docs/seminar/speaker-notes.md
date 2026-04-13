# Speaker Notes

## Opening

This project is a small library management system designed for a school seminar. The goal was to create a working web application that can manage books and loans, and then deploy it inside an Ubuntu virtual machine.

## Architecture

Instead of putting all logic in one file, the project is organized into small service modules. The auth service handles login, the catalog service handles books, and the circulation service handles issuing and returning books. The web application is responsible only for the user interface and request handling. All of these modules run together in one Flask deployment, which keeps the project practical for a school seminar.

## Database

The system uses SQLite because it is lightweight and easy to deploy. There are three main tables: users, books, and loans. Users represent administrators, books represent the library catalog, and loans store issue and return activity.

## Demo Flow

First, I log in as the administrator. Then I can see the list of books in the system. I can add a new book, issue a book to a borrower, and return it. When a book is issued, the available inventory decreases. When it is returned, the inventory increases again.

## Deployment

The system can be deployed in an Ubuntu virtual machine by installing Python, cloning the repository, creating a virtual environment, installing the dependencies, seeding demo data, and running the Flask application. This makes the project easy to reproduce for the seminar.

## Closing

In conclusion, the project demonstrates a full workflow from design to deployment. It solves a real administrative problem, uses a modular structure, and can be expanded in the future with more features such as search, student accounts, and overdue notifications.
