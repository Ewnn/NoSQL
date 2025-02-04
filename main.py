import redis

# Connexion à Redis (par défaut localhost et port 6379)
r = redis.Redis(host='localhost', port=6379, db=0)

# Ajouter des clés à Redis
r.set('user:1:name', 'John Doe')
r.set('user:1:email', 'john.doe@example.com')
r.setex('session_key', 3600, 'session_data')

# Récupérer des valeurs à partir de Redis
user_name = r.get('user:1:name')
user_email = r.get('user:1:email')

# Décoder les valeurs en bytes pour les convertir en chaînes de caractères
user_name = user_name.decode('utf-8')
user_email = user_email.decode('utf-8')

print(f'Nom de l\'utilisateur: {user_name}')
print(f'Email de l\'utilisateur: {user_email}')

# Récupérer plusieurs clés en une seule fois
keys = ['user:1:name', 'user:1:email']
values = r.mget(keys)

# Convertir les valeurs en bytes en chaînes de caractères
values = [value.decode('utf-8') for value in values]

print('Valeurs des clés récupérées:', values)
