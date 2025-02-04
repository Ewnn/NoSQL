from pymongo import MongoClient

# Connexion à MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client.mydb
collection = db.mycollection

# Create (Insert) : Insérer un seul document
document = {"name": "John Doe", "email": "john.doe@example.com", "age": 30}
result = collection.insert_one(document)
print("Inserted document ID:", result.inserted_id)

# Read (Query) : Récupérer un seul document
query = {"name": "John Doe"}
document = collection.find_one(query)
print(document)

# Update : Mettre à jour un seul document
query = {"name": "John Doe"}
update = {"$set": {"age": 31}}  # Modifier l'âge
result = collection.update_one(query, update)
print("Modified document count:", result.modified_count)

# Read (Query) : Récupérer un seul document
query = {"name": "John Doe"}
document = collection.find_one(query)
print(document)

# Delete : Supprimer un seul document
query = {"name": "John Doe"}
result = collection.delete_one(query)
print("Deleted document count:", result.deleted_count)
