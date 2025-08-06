from pymongo import MongoClient
from ..config import Config  # import Config from the common package

# Initialize MongoDB client using the connection details from Config
client = MongoClient(Config.MONGO_URI)
db = client.get_database(Config.MONGO_DBNAME)

# Collections used by the auth service
users_db = db.get_collection('users')
logs_db = db.get_collection('logs')
