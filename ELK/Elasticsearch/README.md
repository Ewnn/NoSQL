# Elasticsearch Installation with Docker

## Installation
To install and run Elasticsearch using Docker, execute the following command in your terminal:

```sh
docker run -p 9200:9200 -p 9300:9300 -d -e "discovery.type=single-node" docker.elastic.co/elasticsearch/elasticsearch:7.14.0
```

### Command Breakdown
- `docker run`: Runs a new container from an image.
- `-p 9200:9200`: Maps port 9200 of the container to port 9200 on the host machine (used for external access).
- `-p 9300:9300`: Maps port 9300 of the container to port 9300 on the host machine (used for cluster communication).
- `-d`: Runs the container in detached mode, allowing it to run in the background.
- `-e "discovery.type=single-node"`: Sets an environment variable in the container, configuring Elasticsearch to run as a single-node cluster (useful for development and testing).
- `docker.elastic.co/elasticsearch/elasticsearch:7.14.0`: Specifies the Elasticsearch image and version to use.

When executed, Docker will download the Elasticsearch image (if not already available), create a container, and start Elasticsearch. The service will be accessible on ports 9200 and 9300.

## Testing Your Installation
### Check Cluster Health
To verify that Elasticsearch is running, execute the following command:

```sh
curl 0.0.0.0:9200/_cluster/health | jq
```

#### Expected Response:
```json
{
  "cluster_name": "docker-cluster",
  "status": "green",
  "timed_out": false,
  "number_of_nodes": 1,
  "number_of_data_nodes": 1,
  "active_primary_shards": 1,
  "active_shards": 1,
  "relocating_shards": 0,
  "initializing_shards": 0,
  "unassigned_shards": 0,
  "delayed_unassigned_shards": 0,
  "number_of_pending_tasks": 0,
  "number_of_in_flight_fetch": 0,
  "task_max_waiting_in_queue_millis": 0,
  "active_shards_percent_as_number": 100
}
```
This command provides information on the cluster's health, including node count, shard status, and overall stability.

### Check Node Information
To retrieve details about the nodes in your cluster, run:

```sh
curl -X GET "http://0.0.0.0:9200/_cat/nodes?v"
```
This command displays a summary of the nodes, including their IP addresses, IDs, and resource usage.

## Create an Index and Insert Data
An index in Elasticsearch is similar to a database in a traditional relational database system.

### Create an Index
To create an index called `cities` with 2 shards and 2 replicas per shard, run:

```sh
curl -XPUT 'http://localhost:9200/cities' -H 'Content-Type: application/json' -d '
{
  "settings": {
    "number_of_shards": 2,
    "number_of_replicas": 2
  }
}'
```
#### Expected Response:
```json
{"acknowledged":true,"shards_acknowledged":true,"index":"cities"}
```

### Retrieve Index Settings
To verify the index settings, run:

```sh
curl -XGET 'http://localhost:9200/cities/_settings' | jq
```
#### Expected Output:
```json
{
  "cities": {
    "settings": {
      "index": {
        "routing": {
          "allocation": {
            "include": {
              "_tier_preference": "data_content"
            }
          }
        },
        "number_of_shards": "2",
        "provided_name": "cities",
        "creation_date": "1678636556321",
        "number_of_replicas": "2",
        "uuid": "vsqBEmHWSBaki2AL-oClsA",
        "version": {
          "created": "7110199"
        }
      }
    }
  }
}
```

### Insert a Document
To add a document representing London in the `cities` index, run:

```sh
curl -XPOST 'http://localhost:9200/cities/_doc' -H 'Content-Type: application/json' -d '
{
  "city": "London",
  "country": "England"
}'
```
#### Expected Response:
```json
{
  "_index": "cities",
  "_type": "_doc",
  "_id": "pquR1oYBQIvdICuNRLuD",
  "_version": 1,
  "result": "created",
  "_shards": {
    "total": 3,
    "successful": 1,
    "failed": 0
  },
  "_seq_no": 1,
  "_primary_term": 1
}
```
This response confirms that the document has been successfully created and assigned a unique ID.

### Retrieve the Inserted Document
To fetch the document by its ID, use:

```sh
curl -XGET 'http://localhost:9200/cities/_doc/{document_id}'
```
#### Expected Output:
```json
{
  "_index": "cities",
  "_type": "_doc",
  "_id": "pquR1oYBQIvdICuNRLuD",
  "_version":1,
  "_seq_no":1,
  "_primary_term":1,
  "found":true,
  "_source": {
    "city": "London",
    "country": "England"
  }
}
```
# Bulk Insert into Elasticsearch

This script performs bulk insertions into an Elasticsearch node for multiple indices. The data for each index is taken from respective JSON files: `receipe.json`, `accounts.json`, `movies.json`, and `products.json`.

## Prerequisites

Make sure you have the following installed:

- **Elasticsearch** running locally on `localhost:9200`.
- **curl** command-line tool.
- Valid JSON files: `receipe.json`, `accounts.json`, `movies.json`, and `products.json`.

## Usage

Run the following commands to insert data into Elasticsearch:

1. **Insert into `receipe` index**:
    ```bash
    curl -s -H "Content-Type: application/x-ndjson" -XPOST localhost:9200/receipe/_bulk --data-binary "@receipe.json" &&\
    printf "\n✅ Insertion receipe index to elastic node OK ✅ "
    ```

2. **Insert into `accounts` index**:
    ```bash
    curl -s -H "Content-Type: application/x-ndjson" -XPOST localhost:9200/accounts/docs/_bulk --data-binary "@accounts.json"
    printf "\n✅ Insertion accounts index to elastic node OK ✅ "
    ```

3. **Insert into `movies` index**:
    ```bash
    curl -s -H "Content-Type: application/x-ndjson" -XPOST localhost:9200/movies/_bulk --data-binary "@movies.json"
    printf "\n✅ Insertion movies index to elastic node OK ✅ "
    ```

4. **Insert into `products` index**:
    ```bash
    curl -s -H "Content-Type: application/x-ndjson" -XPOST localhost:9200/products/_bulk --data-binary "@products.json"
    printf "\n✅ Insertion products index to elastic node OK ✅ "
    ```

## Verify the Insertion

After performing the bulk insertions, you can verify the data has been inserted into the `accounts` index by running the following command:
1. **Verify insertion into `receipe` index**:
    ```bash
    curl -X GET "localhost:9200/receipe/_search?pretty"
    ```

2. **Verify insertion  `accounts` index**:
    ```bash
    curl -X GET "localhost:9200/accounts/_search?pretty"
    ```

3. **Verify insertion  `movies` index**:
    ```bash
    curl -X GET "localhost:9200/movies/_search?pretty"
    ```

4. **Verify insertion  `products` index**:
    ```bash
    curl -X GET "localhost:9200/products/_search?pretty"
    ```


# TP : Opérations CRUD avec Elasticsearch

## 1. Vérifier que Elasticsearch fonctionne
Avant de commencer, assure-toi que ton serveur Elasticsearch est bien en marche avec la commande suivante :
```bash
curl -X GET "http://localhost:9200"
```
Ou dans Kibana Dev Tools :
```json
GET /
```
Si Elasticsearch est actif, il renverra des informations sur la version et le cluster.

---

## 2. Créer un document dans l’index `receipe`
Ajoute une nouvelle recette en envoyant la requête suivante :
```bash
curl -X POST "http://localhost:9200/receipe/_doc" -H "Content-Type: application/json" -d '{
  "created": "2022/03/12 12:00:00",
  "title": "Chocolate Cake",
  "description": "A rich and decadent chocolate cake recipe",
  "preparation_time_minutes": 60,
  "servings": {
    "min": 8,
    "max": 10
  },
  "ingredients": [
    { "name": "flour", "quantity": "2 cups" },
    { "name": "sugar", "quantity": "2 cups" },
    { "name": "cocoa powder", "quantity": "3/4 cup" },
    { "name": "baking powder", "quantity": "2 teaspoons" },
    { "name": "baking soda", "quantity": "2 teaspoons" },
    { "name": "salt", "quantity": "1 teaspoon" },
    { "name": "buttermilk", "quantity": "1 cup" },
    { "name": "vegetable oil", "quantity": "1/2 cup" },
    { "name": "eggs", "quantity": "2" },
    { "name": "vanilla extract", "quantity": "2 teaspoons" },
    { "name": "boiling water", "quantity": "1 cup" }
  ],
  "steps": "1. Preheat oven to 350 degrees F (175 degrees C)..."
}'
```
Ou dans Kibana Dev Tools :
```json
POST receipe/_doc
{
  "created": "2022/03/12 12:00:00",
  "title": "Chocolate Cake",
  "description": "A rich and decadent chocolate cake recipe",
  "preparation_time_minutes": 60
}
```
✅ **Résultat attendu** : Un document est créé avec un ID généré automatiquement.

---

## 3. Créer un document avec un ID spécifique
Si tu veux attribuer un ID précis, par exemple `9999`, utilise :
```bash
curl -X POST "http://localhost:9200/receipe/_doc/9999" -H "Content-Type: application/json" -d '{
  "title": "Chocolate Cake",
  "description": "A delicious chocolate cake recipe",
  "preparation_time_minutes": 60
}'
```
Ou dans Kibana Dev Tools :
```json
POST receipe/_doc/9999
{
  "title": "Chocolate Cake",
  "description": "A delicious chocolate cake recipe",
  "preparation_time_minutes": 60
}
```
✅ **Résultat attendu** : Un document est créé avec l'ID `9999`.

---

## 4. Lire un document spécifique
Pour récupérer un document, utilise son ID :
```bash
curl -X GET "http://localhost:9200/receipe/_doc/9999"
```
Ou dans Kibana Dev Tools :
```json
GET receipe/_doc/9999
```
✅ **Résultat attendu** : Retourne le contenu du document.

---

## 5. Mettre à jour un document
Pour modifier un champ (ex. ajouter une description plus détaillée), utilise :
```bash
curl -X POST "http://localhost:9200/receipe/_update/9999" -H "Content-Type: application/json" -d '{
  "doc": {
    "description": "A rich and decadent chocolate cake with layers of buttercream frosting"
  }
}'
```
Ou dans Kibana Dev Tools :
```json
POST receipe/_update/9999
{
  "doc": {
    "description": "A rich and decadent chocolate cake with layers of buttercream frosting"
  }
}
```
✅ **Résultat attendu** : Le champ `description` est mis à jour.

---

## 6. Supprimer un document
Si tu veux supprimer une recette par ID, utilise :
```bash
curl -X DELETE "http://localhost:9200/receipe/_doc/9999"
```
Ou dans Kibana Dev Tools :
```json
DELETE receipe/_doc/9999
```
✅ **Résultat attendu** : Le document est supprimé.

---

## 7. Vérifier tous les documents dans l’index
Pour voir tous les documents enregistrés dans `receipe`, utilise :
```bash
curl -X GET "http://localhost:9200/receipe/_search?pretty"
```
Ou dans Kibana Dev Tools :
```json
GET receipe/_search
```
Cela affichera toutes les recettes enregistrées.
