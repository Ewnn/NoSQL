#!/bin/bash

docker run \
    --name my_neo4j \
    -p7474:7474 -p7687:7687 \
    -v ~/neo4j_data:/data \
    -e NEO4J_AUTH=neo4j/password \
    -d neo4j

# Attendre que le conteneur soit complètement démarré
sleep 2

# Exécuter le script Python pour la connexion à Neo4j
python3 connectPythonToNeo4j.py

# Attendre 2 secondes après l'exécution du script Python
sleep 2

# Arrêter et supprimer le conteneur Neo4j
docker stop my_neo4j
docker rm my_neo4j
