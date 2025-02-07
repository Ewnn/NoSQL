#!/bin/bash

# Démarrer le conteneur MongoDB
docker run --name my_mongo -p 27017:27017 -d mongo

# Attendre que le conteneur soit complètement démarré
sleep 2

# Exécuter le script Python pour la connexion à MongoDB
echo "Single doc CRUD";
python3 CRUD_Single_Doc.py

# Attendre 2 secondes après l'exécution du script Python
sleep 2

# Exécuter le script Python pour la connexion à MongoDB
echo "Multiple docs CRUD";
python3 CRUD_Multiple_Docs.py

# Attendre 2 secondes après l'exécution du script Python
sleep 2

# Arrêter et supprimer le conteneur MongoDB
echo "Le conteneur Mongo se stoppe.";
docker stop my_mongo
echo "Le conteneur Mongo est supprimé.";
docker rm my_mongo
