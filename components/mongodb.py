# mongo_utils.py
from pymongo import MongoClient
import datetime
import os


class MongoDBChat:
    def __init__(self, db_name="chat_app", collection_name="chat_history"):
        mongo_uri = os.getenv("MONGO_URI", "mongodb://localhost:27017")
        self.client = MongoClient(mongo_uri)
        self.db = self.client[db_name]
        self.collection = self.db[collection_name]

    def save_chat(self, session_id, messages):
        """Insert or update chat messages for a session"""
        self.collection.update_one(
            {"session_id": session_id},
            {"$set": {
                "messages": messages,
                "timestamp": datetime.datetime.utcnow()
            }},
            upsert=True
        )

    def load_chat(self, session_id):
        """Retrieve chat messages for a session"""
        chat_doc = self.collection.find_one({"session_id": session_id})
        
        if chat_doc:
            return chat_doc.get("messages", [])
        return []

    def list_sessions(self):
        """Get all saved sessions"""
        return [
            doc["session_id"] 
            for doc in self.collection.find({}, {"session_id": 1, "_id":0})]
