echo "Vérification de l'index 'receipe' après truncation..."
count_receipe=$(curl -s -X GET "localhost:9200/receipe/_count" | jq .count)
if [ "$count_receipe" -eq 0 ]; then
  echo -e "\n✅ L'index 'receipe' est vide après truncation ✅"
else
  echo -e "\n❌ L'index 'receipe' contient encore des documents ($count_receipe) ❌"
fi

echo -e "\n"

echo "Vérification de l'index 'accounts' après truncation..."
count_accounts=$(curl -s -X GET "localhost:9200/accounts/_count" | jq .count)
if [ "$count_accounts" -eq 0 ]; then
  echo -e "\n✅ L'index 'accounts' est vide après truncation ✅"
else
  echo -e "\n❌ L'index 'accounts' contient encore des documents ($count_accounts) ❌"
fi

echo -e "\n"

echo "Vérification de l'index 'movies' après truncation..."
count_movies=$(curl -s -X GET "localhost:9200/movies/_count" | jq .count)
if [ "$count_movies" -eq 0 ]; then
  echo -e "\n✅ L'index 'movies' est vide après truncation ✅"
else
  echo -e "\n❌ L'index 'movies' contient encore des documents ($count_movies) ❌"
fi

echo -e "\n"

echo "Vérification de l'index 'products' après truncation..."
count_products=$(curl -s -X GET "localhost:9200/products/_count" | jq .count)
if [ "$count_products" -eq 0 ]; then
  echo -e "\n✅ L'index 'products' est vide après truncation ✅"
else
  echo -e "\n❌ L'index 'products' contient encore des documents ($count_products) ❌"
fi

echo -e "\nVérification terminée pour tous les indices."
