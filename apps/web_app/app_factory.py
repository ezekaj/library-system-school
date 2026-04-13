"""Flask application factory."""

from __future__ import annotations

from flask import Flask, g

from apps.web_app.routes import web_bp
from shared.config import load_settings
from shared.database import create_session, create_tables, initialize_database
from shared.model_loader import load_models


def create_app() -> Flask:
    settings = load_settings()
    initialize_database(settings.database_url)
    create_tables(load_models)

    app = Flask(__name__, template_folder="templates", static_folder="static")
    app.config["SECRET_KEY"] = settings.secret_key
    app.config["DEBUG"] = settings.debug
    app.register_blueprint(web_bp)

    @app.before_request
    def open_session() -> None:
        g.db = create_session()

    @app.teardown_request
    def close_session(_: BaseException | None) -> None:
        session = g.pop("db", None)
        if session is not None:
            session.close()

    return app
