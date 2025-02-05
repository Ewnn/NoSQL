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