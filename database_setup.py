from config import bicycles_collection

# Sample Bicycles
bicycles = [
    {"bike_id": 1, "status": "available", "hourly_rate": 5},
    {"bike_id": 2, "status": "available", "hourly_rate": 6},
    {"bike_id": 3, "status": "rented", "hourly_rate": 5},
]

# Insert into MongoDB
bicycles_collection.insert_many(bicycles)
print("Bicycles added to the database.")
