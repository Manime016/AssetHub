# AssetHub — Asset Management Backend

AssetHub is a Flask and MySQL application for managing employees, company assets and asset assignments.

The project is intentionally backend-focused and demonstrates REST-style application workflows, relational database integration, authentication and modular Flask architecture.

## Tech Stack

- Python
- Flask
- MySQL
- Jinja2
- SQL
- Flask Blueprints

## Core Features

- Employee management
- Asset management
- Asset assignment and return
- Authentication
- Admin management
- Search and filtering
- Dashboard data
- MySQL persistence
- Modular route organization with Flask Blueprints

## Project Structure

```text
AssetHub/
├── database/       # Database connection and query/data-access code
├── routes/         # Flask route blueprints
├── templates/      # Server-rendered views
├── static/         # Frontend assets used to interact with the backend
├── config.py       # Application configuration
├── app.py          # Flask application entry point
└── requirements.txt
```

## Running Locally

Create and activate a virtual environment:

```bash
python -m venv .venv
```

Windows:

```bash
.venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Configure the MySQL connection using the project's configuration/environment settings, create the required database and tables, then start the application:

```bash
python app.py
```

## Engineering Focus

The project demonstrates how a Flask application can separate route handling, database access and application configuration while using MySQL for persistent relational data.

## Project Status

Portfolio project. The primary goal is demonstrating practical Python backend development with Flask and MySQL.
