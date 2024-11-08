import requests

API_KEY = '643317a91e07640cfe015328345dc5b5'
city = "Paris"
url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}"

response = requests.get(url)

# Affiche les données pour voir si la requête a fonctionné
if response.status_code == 200:
    data = response.json()
    print(data)
else:
    print("Erreur dans la requête API:", response.status_code)
