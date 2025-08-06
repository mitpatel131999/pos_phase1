from urllib.parse import quote_plus
import os

class Config:
    SECRET_KEY = os.urandom(24)
    MONGO_USERNAME = 'mitpatelr1999'
    MONGO_PASSWORD = 'Mit@94285'
    ENCODED_USERNAME = quote_plus(MONGO_USERNAME)
    ENCODED_PASSWORD = quote_plus(MONGO_PASSWORD)
    MONGO_URI = f"mongodb+srv://{ENCODED_USERNAME}:{ENCODED_PASSWORD}@cluster0.fdivylq.mongodb.net/?retryWrites=false&w=majority&appName=Cluster0"
    MONGO_DBNAME = 'posdatabase'
