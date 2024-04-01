from requests import get
from bs4 import BeautifulSoup
import json



def return_parameters(link):
    response = get(link)
    soup = BeautifulSoup(response.content, "html.parser")
    header = soup.find('h1', class_="product__title").text
    price = soup.find('div', class_="product__price-actual").text
    return {'link':link, 'header':header, 'price':price}


list_of_results = []

with open('shampuni-petslike.json') as reader:
    list_of_links = json.load(reader)
    for link in list_of_links:
        list_of_results.append(return_parameters(link))

with open('shampuni-petslike_downladed_result.json', 'w') as writer:
    json.dump(list_of_results, writer,  indent=4)


