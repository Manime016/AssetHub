# app.py
from flask import Flask
from routes.pages import pages  # Import blueprint cleanly
from config import Config  # Import config settings
from database.connection import get_db_connection  # Import DB connection function
from routes.employee import employee_bp
from routes.login import login_bp
from routes.asset import asset_bp
from routes.admin import admin_bp
from routes.contact import contact_bp

app = Flask(__name__)
app.config.from_object(Config)

# Register the blueprints with app
app.register_blueprint(pages)
app.register_blueprint(employee_bp)  # <--- ADDED THIS LINE TO FIX THE ERROR
app.register_blueprint(login_bp)  # <--- ADDED THIS LINE TO FIX THE ERROR
app.register_blueprint(asset_bp)
app.register_blueprint(admin_bp)
app.register_blueprint(contact_bp)

if __name__ == "__main__":
    app.run(debug=True)