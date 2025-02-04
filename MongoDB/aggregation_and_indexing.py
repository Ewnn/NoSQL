# Pipeline d'agrégation pour compter les personnes par âge supérieur à 25
pipeline = [
    {"$match": {"age": {"$gt": 25}}},  # Filtrer les âges supérieurs à 25
    {"$group": {"_id": "$age", "count": {"$sum": 1}}}  # Compter le nombre d'individus par âge
]

# Exécuter l'agrégation
results = collection.aggregate(pipeline)

# Afficher les résultats
print("Count of accounts by age greater than 25:")
for result in results:
    print(result)
