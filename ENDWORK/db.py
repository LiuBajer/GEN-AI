from pymongo import MongoClient
from bson import ObjectId

client = MongoClient("mongodb://localhost:27017/")
db = client["clothing_advisor"]
users = db["users"]

def add_user(data):
    return users.insert_one(data)

def get_due_users(current_hour):
    return list(users.find({"notification_hour": current_hour}))

def update_user(user_id, new_data):
    users.update_one({"_id": ObjectId(user_id)}, {"$set": new_data})

def remove_user(user_id):
    users.delete_one({"_id": ObjectId(user_id)})