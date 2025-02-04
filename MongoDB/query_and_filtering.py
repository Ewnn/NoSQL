# import json
# from pymongo import MongoClient

# # Connect to MongoDB
# client = MongoClient("mongodb://localhost:27017/")  
# db = client.mydb 
# collection = db.mycollection  

# # Load data from the JSON file
# with open("accounts.json", "r") as file:
#     data = json.load(file)  

# # Insert the data into MongoDB
# result = collection.insert_many(data)  
# print("Inserted data with the following IDs:", result.inserted_ids)  

# # Create an index on the 'address.city' field for faster queries
# index_name = "city_index" 
# collection.create_index("address.city", name=index_name)  

# # Query to find all accounts from a specific city
# city = "Bradshawborough"  
# results = collection.find({"address.city": city})  

# # Print the results of the query
# for result in results:
#     print(result)  

# # Query to find all accounts with a balance greater than a specific value
# min_balance = 30000  
# results = collection.find({"balance": {"$gt": min_balance}}) 

# # Print the results of the balance query
# for result in results:
#     print(result)  

# # Perform aggregation to calculate the total balance for each city
# pipeline = [
#     {"$group": {"_id": "$address.city", "total_balance": {"$sum": "$balance"}}}, 
#     {"$sort": {"total_balance": -1}}  
# ]

# results = collection.aggregate(pipeline) 

import json
from pymongo import MongoClient

# Connect to MongoDB
client = MongoClient("mongodb://localhost:27017/")  
db = client.mydb2 
collection = db.mycollection  

# Load data from the JSON file
with open("accounts.json", "r") as file:
    data = json.load(file)  

# Insert the data into MongoDB
result = collection.insert_many(data)  
print("Inserted data with the following IDs:", result.inserted_ids)  

# Create an index on the 'address.city' field for faster queries
index_name = "city_index" 
collection.create_index("address.city", name=index_name)  

# Create an index on the 'email' field, ensuring uniqueness
email_index_name = collection.create_index("email", unique=True)
print(f"Created unique index on 'email' with index name: {email_index_name}")

# Query to find all accounts from a specific city
city = "Bradshawborough"  
results = collection.find({"address.city": city})  

# Print the results of the query
for result in results:
    print(result)  

# Query to find all accounts with a balance greater than a specific value
min_balance = 30000  
results = collection.find({"balance": {"$gt": min_balance}}) 

# Print the results of the balance query
for result in results:
    print(result)  

# Perform aggregation to calculate the total balance for each city
pipeline = [
    {"$group": {"_id": "$address.city", "total_balance": {"$sum": "$balance"}}}, 
    {"$sort": {"total_balance": -1}}  
]

results = collection.aggregate(pipeline)

# Print the results of the aggregation
for result in results:
    print(result)

# Perform aggregation to count accounts based on age greater than 25
pipeline_age = [
    {"$match": {"age": {"$gt": 25}}},  # Match accounts where age > 25
    {"$group": {"_id": "$age", "count": {"$sum": 1}}}  # Group by age and count
]

results_age = collection.aggregate(pipeline_age)

# Print the results of the age aggregation
for result in results_age:
    print(result)
