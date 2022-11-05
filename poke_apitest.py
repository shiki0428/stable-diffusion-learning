import requests

url = "https://pokeapi.co/api/v2/pokemon/pikachu/"
url = "https://pokeapi.co/api/v2/pokemon/"

r = requests.get(url, timeout=5)
r = r.json()


print(r)

# name  = r['name']
# id    = r['id']
# image = r['sprites']['front_default']
# types = r['types'][0]['type']['name']

# print(id)
# print(name)
# print(image)
# print(types)