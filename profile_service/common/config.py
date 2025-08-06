import os
from urllib.parse import quote_plus


class Config:
    """Configuration for the profile microservice.
    Values are pulled from environment variables with sensible defaults.
    """

    MONGO_USER = os.environ.get("MONGO_USER", "posadmin")
    MONGO_PASSWORD = quote_plus(os.environ.get("MONGO_PASSWORD", "posadmin"))
    MONGO_HOST = os.environ.get("MONGO_HOST", "localhost")
    MONGO_PORT = os.environ.get("MONGO_PORT", "27017")
    MONGO_DB = os.environ.get("MONGO_DB", "posdb")

    # Secret keys for Flask and JWT.  In production these should be
    # provided via environment variables or a secrets manager.
    SECRET_KEY = os.environ.get("SECRET_KEY") or os.urandom(24)
    JWT_SECRET_KEY = os.environ.get("JWT_SECRET_KEY") or SECRET_KEY

    # Construct the MongoDB connection URI
    MONGO_URI = (
        f"mongodb://{MONGO_USER}:{MONGO_PASSWORD}@{MONGO_HOST}:{MONGO_PORT}/"
        f"{MONGO_DB}?authSource=admin"
    )
