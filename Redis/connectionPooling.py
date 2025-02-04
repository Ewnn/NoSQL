import redis
from redis import ConnectionPool
import threading
import time

# Crée un pool de connexions Redis
pool = ConnectionPool(host='localhost', port=6379, db=0, max_connections=10)

# Fonction qui sera exécutée par chaque thread
def worker(thread_id):
    # Crée une instance de Redis avec le pool de connexions
    r = redis.Redis(connection_pool=pool)
    
    # Effectuer des opérations Redis, par exemple, ajout d'une clé
    key = f"user:{thread_id}:name"
    r.set(key, f"Thread {thread_id}")
    time.sleep(1)  # Simuler une opération de longue durée
    value = r.get(key)
    print(f"Thread {thread_id} a récupéré la valeur: {value.decode('utf-8')}")

# Crée plusieurs threads pour tester le pooling de connexions
threads = []
for i in range(10):  # 10 threads
    thread = threading.Thread(target=worker, args=(i,))
    threads.append(thread)
    thread.start()

# Attendre que tous les threads aient terminé
for thread in threads:
    thread.join()
