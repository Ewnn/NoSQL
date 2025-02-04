**Télécharger l’image Redis depuis Docker Hub** :  
   ```sh
   docker pull redis
   ```

**Lancer un conteneur Redis en arrière-plan** :  
   ```sh
   docker run --name my-redis -d redis
   ```
   - `--name my-redis` : Nom du conteneur  
   - `-d` : Exécute le conteneur en mode détaché (en arrière-plan)

**Vérifier que le conteneur est bien en cours d’exécution** :  
   ```sh
   docker ps
   ```
   Cette commande liste les conteneurs en cours d'exécution.

**Se connecter à Redis via le client en ligne de commande (`redis-cli`)** :  
   ```sh
   docker exec -it my-redis redis-cli
   ```
   - `exec -it` : Ouvre une session interactive  
   - `redis-cli` : Lance le client Redis pour interagir avec la base de données  
