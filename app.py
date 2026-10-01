from flask import Flask

from config import Config
from routes.pages import pages
from routes.employee import employee_bp
from routes.login import login_bp
from routes.asset import asset_bp
from routes.admin import admin_bp
from routes.contact import contact_bp


app = Flask(__name__)
app.config.from_object(Config)

app.register_blueprint(pages)
app.register_blueprint(employee_bp)
app.register_blueprint(login_bp)
app.register_blueprint(asset_bp)
app.register_blueprint(admin_bp)
app.register_blueprint(contact_bp)


if __name__ == "__main__":
    app.run(debug=app.config["DEBUG"])
