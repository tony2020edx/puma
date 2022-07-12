import requests
from bs4 import BeautifulSoup
import csv
import time
import random

all_product_urls = []

base_url = 'https://www.adidas.co.in/sneakers'

web_page = requests.get(base_url)
soup = BeautifulSoup(web_page.content, 'html.parser')

for link in soup.find_all('a', class_= "glass-product-card__assets-link"):

    pdp_url = link.get('href')
    pdp_url = "https://www.adidas.co.in/" + pdp_url

    all_product_urls.append(pdp_url)
    print(pdp_url)


