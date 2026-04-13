"""Web routes."""

from __future__ import annotations

from flask import Blueprint, redirect, url_for


web_bp = Blueprint("web", __name__)


@web_bp.get("/")
def index():
    return redirect(url_for("web.health"))


@web_bp.get("/health")
def health():
    return {"status": "ok"}
