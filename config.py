from pymongo import MongoClient

# MongoDB Connection
client = MongoClient("mongodb://localhost:27017/")
db = client["bicycle_rental"]

# Collections
users_collection = db["users"]
bicycles_collection = db["bicycles"]
rentals_collection = db["rentals"]

from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client["bicycle_rental"]

users_collection = db["users"]
bicycles_collection = db["bicycles"]
rentals_collection = db["rentals"]
messages_collection = db["messages"]  # New collection for Contact Us messages
