from pymongo import MongoClient

# Connect to MongoDB Compass
client = MongoClient("mongodb://localhost:27017/")

# Create a database
db = client["rental_bicycles"]

# Create a collection (table)
users_collection = db["users"]
