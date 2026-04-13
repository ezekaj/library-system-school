"""Web routes."""

from __future__ import annotations

from functools import wraps

from flask import Blueprint, flash, g, redirect, render_template, request, session, url_for

from services.auth_service.service import authenticate_admin, get_authenticated_user
from services.catalog_service.service import create_book, get_catalog_book, list_catalog_books
from services.circulation_service.service import issue_book, list_open_loans, return_book


web_bp = Blueprint("web", __name__)


def login_required(view):
    @wraps(view)
    def wrapped_view(*args, **kwargs):
        if session.get("user_id") is None:
            flash("Please sign in to continue.", "error")
            return redirect(url_for("web.login"))
        return view(*args, **kwargs)

    return wrapped_view


def current_user():
    user_id = session.get("user_id")
    if user_id is None:
        return None
    user = get_authenticated_user(g.db, user_id)
    if user is None:
        session.clear()
    return user


def build_loan_rows():
    books = list_catalog_books(g.db)
    book_lookup = {book.id: book for book in books}
    loan_rows = []

    for loan in list_open_loans(g.db):
        book = book_lookup.get(loan.book_id) or get_catalog_book(g.db, loan.book_id)
        loan_rows.append(
            {
                "id": loan.id,
                "borrower_name": loan.borrower_name,
                "book_title": book.title if book else "Unknown Book",
                "issued_at": loan.issued_at,
            }
        )

    return books, loan_rows


@web_bp.get("/")
def index():
    if session.get("user_id") is not None:
        return redirect(url_for("web.dashboard"))
    return redirect(url_for("web.login"))


@web_bp.route("/login", methods=["GET", "POST"])
def login():
    if session.get("user_id") is not None:
        return redirect(url_for("web.dashboard"))

    if request.method == "POST":
        email = request.form.get("email", "")
        password = request.form.get("password", "")
        user = authenticate_admin(g.db, email, password)

        if user is None:
            flash("Invalid email or password.", "error")
        else:
            session.clear()
            session["user_id"] = user.id
            session["user_name"] = user.name
            flash("Login successful.", "success")
            return redirect(url_for("web.dashboard"))

    return render_template("login.html")


@web_bp.post("/logout")
@login_required
def logout():
    session.clear()
    flash("You have been signed out.", "success")
    return redirect(url_for("web.login"))


@web_bp.get("/dashboard")
@login_required
def dashboard():
    user = current_user()
    if user is None:
        return redirect(url_for("web.login"))

    books, loan_rows = build_loan_rows()
    return render_template("dashboard.html", books=books, loan_rows=loan_rows, user=user)


@web_bp.post("/books")
@login_required
def add_book():
    try:
        total_copies = int(request.form.get("total_copies", "1"))
        create_book(
            g.db,
            title=request.form.get("title", ""),
            author=request.form.get("author", ""),
            description=request.form.get("description", ""),
            total_copies=total_copies,
        )
        flash("Book added successfully.", "success")
    except ValueError as exc:
        flash(str(exc), "error")

    return redirect(url_for("web.dashboard"))


@web_bp.post("/loans")
@login_required
def create_loan():
    user = current_user()
    if user is None:
        return redirect(url_for("web.login"))

    try:
        issue_book(
            g.db,
            book_id=int(request.form.get("book_id", "0")),
            borrower_name=request.form.get("borrower_name", ""),
            issued_by_user_id=user.id,
        )
        flash("Book issued successfully.", "success")
    except ValueError as exc:
        flash(str(exc), "error")

    return redirect(url_for("web.dashboard"))


@web_bp.post("/loans/<int:loan_id>/return")
@login_required
def complete_return(loan_id: int):
    try:
        return_book(g.db, loan_id)
        flash("Book returned successfully.", "success")
    except ValueError as exc:
        flash(str(exc), "error")

    return redirect(url_for("web.dashboard"))


@web_bp.get("/health")
def health():
    return {"status": "ok"}
