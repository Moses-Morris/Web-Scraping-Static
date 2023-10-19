# Documentation

## Overview

This Python script performs web scraping on the specified URL `https://greenspoon.co.ke/product-category/fruit-veg/fresh-herbs/`. It extracts data about products listed on the webpage, including product names, currency symbols, and prices. The script utilizes the `requests` library for making HTTP requests and `BeautifulSoup` for parsing HTML content.

## Code Description

```python
import requests
from bs4 import BeautifulSoup

url = 'https://greenspoon.co.ke/product-category/fruit-veg/fresh-herbs/'

# Send an HTTP GET request to the specified URL and retrieve the webpage content
response = requests.get(url).text

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(response, 'lxml')

# Extract specific data from the HTML tags
containers = soup.find_all('div', class_="uael-woo-products-summary-wrap")
for container in containers:
    name = container.find('h2', class_="woocommerce-loop-product__title").text
    priceSymbol = container.find('span', class_="woocommerce-Price-currencySymbol").text
    price = container.find('span', class_="woocommerce-Price-amount amount").text

    # Print extracted data
    print("{}  = {} : {}".format(name, priceSymbol, price))
