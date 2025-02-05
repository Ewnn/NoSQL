echo "Vérification de l'index 'receipe'..."
curl -X GET "localhost:9200/receipe/_search?pretty"
echo -e "\n✅ Fin de la vérification pour 'receipe' ✅\n"

echo "Vérification de l'index 'accounts'..."
curl -X GET "localhost:9200/accounts/_search?pretty"
echo -e "\n✅ Fin de la vérification pour 'accounts' ✅\n"

echo "Vérification de l'index 'movies'..."
curl -X GET "localhost:9200/movies/_search?pretty"
echo -e "\n✅ Fin de la vérification pour 'movies' ✅\n"

echo "Vérification de l'index 'products'..."
curl -X GET "localhost:9200/products/_search?pretty"
echo -e "\n✅ Fin de la vérification pour 'products' ✅\n"

echo "Vérification terminée pour tous les index."