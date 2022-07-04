import requests
from bs4 import BeautifulSoup
import csv

start_url = "https://in.puma.com/in/en/collections/collections-football/collections-football-manchester-city-fc"

web_page = requests.get(start_url)
soup = BeautifulSoup(web_page.content, 'html.parser')

product_links = []

for link in soup.find_all('a', class_='product-tile-title product-tile__title pdp-link line-item-limited line-item-limited--2'):
    if link['href'] not in product_links:
        product_links.append('https://in.puma.com/' + link['href'])

with open('puma_manchester_city.csv', 'w') as csv_file:

    writer = csv.writer(csv_file)
    writer.writerow(['Product Name', 'Price', 'Description', 'Link'])

    for product_url in product_links:
        product_page = requests.get(product_url)
        product_soup = BeautifulSoup(product_page.content, 'html.parser')
        product_name = product_soup.find('h1', class_='product-name').text.strip()
        price = product_soup.find('span', class_='value').text
        product_description = product_soup.find('div', class_='content', itemprop="description").text
        writer.writerow([product_name, price, product_description, product_url])

