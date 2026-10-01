import os

from dotenv import load_dotenv

load_dotenv()


class Config:
    SECRET_KEY = os.getenv("SECRET_KEY")
    MYSQL_HOST = os.getenv("MYSQL_HOST", "localhost")
    MYSQL_PORT = int(os.getenv("MYSQL_PORT", "3306"))
    MYSQL_USER = os.getenv("MYSQL_USER")
    MYSQL_PASSWORD = os.getenv("MYSQL_PASSWORD")
    MYSQL_DB = os.getenv("MYSQL_DB", "AssetHub")
    DEBUG = os.getenv("FLASK_DEBUG", "false").lower() == "true"

    if not SECRET_KEY:
        raise RuntimeError("SECRET_KEY is required")
    if not MYSQL_USER:
        raise RuntimeError("MYSQL_USER is required")
    if not MYSQL_PASSWORD:
        raise RuntimeError("MYSQL_PASSWORD is required")
