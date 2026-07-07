# app.py
from flask import Flask
from routes.pages import pages  # Import blueprint cleanly
from config import Config  # Import config settings
app = Flask(__name__)
app.config.from_object(Config)

        # Register the blueprint with app
app.register_blueprint(pages)

if __name__ == "__main__":
    app.run(debug=True)