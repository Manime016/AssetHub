import os

from flask import Flask

from config import Config
from routes.pages import pages
from routes.employee import employee_bp
from routes.login import login_bp
from routes.asset import asset_bp
from routes.admin import admin_bp
from routes.contact import contact_bp


def create_app() -> Flask:
    app = Flask(__name__)
    app.config.from_object(Config)

    app.register_blueprint(pages)
    app.register_blueprint(employee_bp)
    app.register_blueprint(login_bp)
    app.register_blueprint(asset_bp)
    app.register_blueprint(admin_bp)
    app.register_blueprint(contact_bp)

    @app.get("/health")
    def health() -> tuple[dict[str, str], int]:
        return {"status": "ok"}, 200

    return app


app = create_app()


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=int(os.getenv("PORT", "5000")),
        debug=app.config["DEBUG"],
    )
