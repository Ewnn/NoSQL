import warnings
from elasticsearch import Elasticsearch
warnings.filterwarnings('ignore')

# Connexion à Elasticsearch avec un délai d'attente augmenté (par exemple 60 secondes)
es = Elasticsearch('http://localhost:9200', timeout=60)

# Créer un index (ignorer l'erreur si l'index existe déjà)
es.indices.create(index="first_index", ignore=400)

# Vérifier si l'index existe
exists = es.indices.exists(index="first_index")
print(exists)  # Cela retournera True si l'index existe, sinon False

# Supprimer l'index (ignorer l'erreur si l'index n'existe pas)
deleted = es.indices.delete(index="first_index", ignore=[400, 404])
print(deleted)  # Cela retournera des informations sur l'index supprimé

# Documents à insérer dans l'index "cities"
doc1 = {"city": "New Delhi", "country": "India"}
doc2 = {"city": "London", "country": "England"}
doc3 = {"city": "Los Angeles", "country": "USA"}

# Insérer doc1 avec id=1
es.index(index="cities", doc_type="places", id=1, body=doc1)

# Insérer doc2 avec id=2
es.index(index="cities", doc_type="places", id=2, body=doc2)

# Insérer doc3 avec id=3
es.index(index="cities", doc_type="places", id=3, body=doc3)

# Récupérer le document avec id=2
res = es.get(index="cities", doc_type="places", id=2)
print(res)

# Afficher uniquement les informations de la ville et du pays
city_info = res['_source']
print(city_info)  # Cela affichera {'city': 'London', 'country': 'England'}

def check_index_exists(index_name):
    # Vérifier si l'index existe
    return es.indices.exists(index=index_name)

# Tester la fonction
index_exists = check_index_exists("first_index")
print(index_exists)  # True si l'index existe, sinon False
