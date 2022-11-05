import requests
import csv

url = "https://pokeapi.co/api/v2/pokemon/?limit=1154&offset="

r = requests.get(url, timeout=5)
r = r.json()

result = r["results"]


def insert_csv():

    with open('pokemon_name_list.csv', 'w') as f:
        writer = csv.writer(f)
        writer.writerow(['number', 'name'])




    with open('pokemon_name_list.csv', 'a') as f:
        for i in result:
            url = i["url"]
            req = requests.get(url)
            req = req.json()
            name  = req['name']
            id    = req['id']
            writer = csv.writer(f)
            writer.writerow([id,name])


# insert_csv()
