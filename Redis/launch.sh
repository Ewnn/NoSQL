#!/bin/bash

# Nom du conteneur
CONTAINER_NAME="my-redis"

# Vérifier si Docker est installé
docker --version &> /dev/null
if [ $? -ne 0 ]; then
    echo "Docker n'est pas installé. Veuillez l'installer avant d'exécuter ce script."
    exit 1
fi

# Vérifier si le conteneur existe déjà
if [ $(docker ps -aq -f name=^${CONTAINER_NAME}$) ]; then
    echo "Un conteneur avec le nom ${CONTAINER_NAME} existe déjà. Le redémarrage..."
    docker start ${CONTAINER_NAME}
else
    echo "Démarrage du conteneur Redis..."
    docker run --name ${CONTAINER_NAME} -d redis
fi

# Vérifier si le conteneur fonctionne
docker ps | grep ${CONTAINER_NAME} &> /dev/null
if [ $? -eq 0 ]; then
    echo "Le conteneur Redis fonctionne correctement."
else
    echo "Erreur : Le conteneur Redis ne fonctionne pas."
    exit 1
fi

# Connexion au Redis CLI
echo "Connexion au Redis CLI..."
docker exec -i ${CONTAINER_NAME} redis-cli <<EOF

SET username "JohnDoe"
GET username
DEL username

HSET user:1 name "Alice"
HMGET user:1 name
HDEL user:1 name

LPUSH fruits "apple"
RPUSH fruits "banana"
LRANGE fruits 0 -1
LPOP fruits
RPOP fruits

SADD colors "red" "green" "blue"
SMEMBERS colors
SREM colors "green"

ZADD scores 10 "player1" 20 "player2"
ZRANGE scores 0 -1
ZREM scores "player1"

EOF

# Fonction pour arrêter et supprimer le conteneur
stop_and_remove() {
    echo "Arrêt et suppression du conteneur Redis..."
    docker stop ${CONTAINER_NAME} && docker rm ${CONTAINER_NAME}
    echo "Le conteneur Redis a été supprimé."
}

# Vérifier si l'utilisateur veut arrêter et supprimer le conteneur
read -p "Voulez-vous arrêter et supprimer le conteneur Redis ? (y/n) " choice
case "$choice" in 
  y|Y ) stop_and_remove;;
  n|N ) echo "Le conteneur Redis continue de fonctionner.";;
  * ) echo "Réponse invalide. Le conteneur Redis continue de fonctionner.";;
esac
