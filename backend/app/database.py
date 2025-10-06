from pymongo import MongoClient
import os

class MongoDB:
    def __init__(self):
        self.client = None
        self.db = None
    
    def connect(self):
        mongo_uri = os.getenv("MONGO_URI", "mongodb://localhost:27017/")
        db_name = os.getenv("DB_NAME", "number_series_db")
        
        self.client = MongoClient(mongo_uri)
        self.db = self.client[db_name]
        
    
        self.client.admin.command('ping')
        print("Conectado correctamente a MongoDB")
        return self.db

mongodb = MongoDB()