"""
Database helper for the profile microservice.
Initialises a MongoClient using settings from the local Config
class and exposes handles to the collections used by profile
operations (profiles, settings, pending transactions, sessions, users, logs).
"""

from pymongo import MongoClient

# Import Config from the parent package
from ..config import Config


# Create a single MongoClient instance
client = MongoClient(Config.MONGO_URI)

# Reference the application database
_db = client[Config.MONGO_DB]

# Collections used by the profile service
profiles_col = _db["profiles"]
settings_col = _db["settings"]
pending_transactions_col = _db["pending_transactions"]
sessions_col = _db["sessions"]
users_col = _db["users"]
logs_col = _db.get("logs")
