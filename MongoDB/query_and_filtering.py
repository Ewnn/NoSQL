import json
import pymongo

# Connect to MongoDB and select the database and collection
client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["your_database"]
collection = db["accounts"]

# Load JSON data from the file
with open("accounts.json", "r") as file:
    data = json.load(file)

# Insert the data into MongoDB
result = collection.insert_many(data)
print("Inserted data with the following IDs:", result.inserted_ids)

# Create an index on the 'address.city' field
index_name = "city_index"
collection.create_index("address.city", name=index_name)

# Perform queries

# Find all accounts from a specific city
city = "Bradshawborough"
results = collection.find({"address.city": city})

print(f"Accounts from {city}:")
for result in results:
    print(result)

# Find all accounts with a balance greater than a specific value
min_balance = 30000
results = collection.find({"balance": {"$gt": min_balance}})

print(f"Accounts with a balance greater than {min_balance}:")
for result in results:
    print(result)

# Perform aggregations

# Find the total balance for each city
pipeline = [
    {"$group": {"_id": "$address.city", "total_balance": {"$sum": "$balance"}}},
    {"$sort": {"total_balance": -1}}
]
results = collection.aggregate(pipeline)

print("Total balance per city:")
for result in results:
    print(f"{result['_id']}: {result['total_balance']}")
