"""Run the Flask web application with `python -m apps.web_app`."""

from apps.web_app.app_factory import create_app


app = create_app()


if __name__ == "__main__":
    app.run()
