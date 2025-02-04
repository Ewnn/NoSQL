from pymongo import MongoClient

# Connexion à MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client.mydb
collection = db.mycollection

# Create (Insert) : Insérer plusieurs documents
documents = [
    {"name": "Alice", "email": "alice@example.com", "age": 25},
    {"name": "Bob", "email": "bob@example.com", "age": 35}
]
result = collection.insert_many(documents)
print("Inserted document IDs:", result.inserted_ids)

# Read (Query) : Récupérer plusieurs documents
query = {"age": {"$gt": 25}}  
documents = collection.find(query)

for doc in documents:
    print(doc)

# Update : Mettre à jour plusieurs documents
query = {"age": {"$gt": 25}}  # Trouver les documents où l'âge est supérieur à 25
update = {"$inc": {"age": 1}}  
result = collection.update_many(query, update)
print("Modified document count:", result.modified_count)

# Delete : Supprimer plusieurs documents
query = {"age": {"$gt": 25}}
result = collection.delete_many(query)
print("Deleted document count:", result.deleted_count)
