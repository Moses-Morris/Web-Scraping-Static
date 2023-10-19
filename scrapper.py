import requests
import bs4
from bs4 import BeautifulSoup
import requests
print(bs4.__version__)


url = 'https://greenspoon.co.ke/product-category/fruit-veg/fresh-herbs/'

response = requests.get(url).text

soup = BeautifulSoup(response, 'lxml')
#print(soup.prettify())

print(soup.find('span', class_ ="uael-woo-product-category"))
print(soup.find_all('h2', class_ ="woocommerce-loop-product__title"))

#print(soup.get_text())
