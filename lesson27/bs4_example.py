from requests import get

from bs4 import BeautifulSoup


response = get('https://petslike.ua/purina-original-sukhii-povnoratsionnii-korm-dlia-doroslikh-kotiv-z-kurkoiu')
soup = BeautifulSoup(response.content, "html.parser")
features = soup.find_all('a', class_="details__link js-details-link")
list_of_links = []
for feature in features:
    #list_of_links.append(str(feature).split('href="')[1].split('">')[0])
    list_of_links.append(feature.attrs['href'])
print(list_of_links)
price = soup.find('div', class_="product__price-old")

pass

pass
