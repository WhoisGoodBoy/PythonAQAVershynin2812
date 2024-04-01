from requests import get
from bs4 import BeautifulSoup
import json

list_of_links = []
pagination_list = []
response = get('https://petslike.ua/category/koti/gigiiena-petslike/shampuni-petslike')
soup = BeautifulSoup(response.content, "html.parser")
pag_div = soup.find('div', class_="pagination__list")
pag_links = pag_div.find_all('a', class_="pagination__number", )
for pagin_link in pag_links:
    pagination_list.append(pagin_link.attrs['href'])


def return_links(category_link):
    response = get(category_link)
    soup = BeautifulSoup(response.content, "html.parser")
    features = soup.find('div', class_="catalog__item")
    links = features.find_all('a', class_="card__title")
    for link in links:
        list_of_links.append(link.attrs['href'])


for page in pagination_list:
    return_links(page)


with open('shampuni-petslike.json', 'w') as writer:
    json.dump(list_of_links, writer,  indent=4)

print(list_of_links, len(list_of_links))
print(pagination_list)


#'class_="catalog__item"'



