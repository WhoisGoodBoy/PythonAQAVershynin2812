import requests
import json

headers = {'ContentType':"application/json"}
url = 'https://swapi.dev/api/'
response = requests.get(url + 'starships/', headers=headers)
print(response.json())
with open('starships.json', 'w') as starships:
    json.dump(response.json(), starships, indent=4)