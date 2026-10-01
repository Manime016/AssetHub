# AssetHub

A Flask + MySQL asset management application for tracking employees, company assets and asset assignments.

AssetHub is intentionally backend-oriented. It demonstrates relational data modeling, authentication, role-based administration, CRUD workflows, search/filtering and modular Flask application structure.

## Stack

- Python
- Flask
- MySQL
- mysql-connector-python
- Jinja2
- Flask Blueprints
- python-dotenv

## Features

- Employee management
- Asset management
- Asset assignment and return
- Authentication
- Admin management
- Search and filtering
- Dashboard views
- MySQL persistence
- Modular blueprint-based routing

## Structure

```text
AssetHub/
├── database/       # MySQL connection and data-access code
├── routes/         # Flask blueprints
├── templates/      # Server-rendered views
├── static/         # Browser assets
├── config.py       # Environment-backed configuration
├── app.py          # Application entrypoint
├── .env.example
└── requirements.txt
```

## Configuration

Create a local environment file from `.env.example`:

```text
SECRET_KEY=your_secret
FLASK_DEBUG=false
MYSQL_HOST=localhost
MYSQL_USER=your_user
MYSQL_PASSWORD=your_password
MYSQL_DB=AssetHub
```

`.env` is ignored by Git. Never commit database passwords or production secrets.

## Run Locally

```bash
python -m venv .venv
```

Windows:

```bash
.venv\Scripts\activate
```

macOS/Linux:

```bash
source .venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Create the required MySQL database/tables, configure `.env`, then start the application:

```bash
python app.py
```

## Engineering Focus

The project separates Flask route handling, database access and configuration instead of putting database operations directly into templates or the application entrypoint. This makes the codebase easier to reason about and extend.

## Project Status

Portfolio project demonstrating practical Python backend development with Flask and MySQL.
