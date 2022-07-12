import requests
from bs4 import BeautifulSoup
import csv
import time
import random

user_agent_list = [
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36',
    'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.71 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/11.1.2 Safari/605.1.15',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_6_8) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.112 Safari/537.36'
]


def time_delay():  # code to add a time delay between requests
    list1 = [1, 2, 2.6, 2.8, 3.1, 3.6, 4, 4.5, 5.5, 6]
    x = random.choice(list1)
    time.sleep(x)


def get_u_a():  # get a random user agent
    user_agent = random.choice(user_agent_list)
    headers = {'User-Agent': user_agent}

    return headers


def clean_price(text_data):
    text_data = text_data.replace("₹", "")
    text_data = text_data.replace(",", "")

    return text_data


def clean_description(description):
    description = description.replace("PRODUCT STORY", "")
    description = description.split("Manufacturer's address")[0]
    description = description.split("Care Instructions")[0]
    description = description.split("Material Information")[0]
    return description


start_url = "https://in.puma.com/in/en/collections/collections-football/collections-football-manchester-city-fc"

web_page = requests.get(start_url, headers=get_u_a())
soup = BeautifulSoup(web_page.content, 'html.parser')

product_links = []

for link in soup.find_all('a',
                          class_='product-tile-title product-tile__title pdp-link line-item-limited line-item-limited--2'):
    if link['href'] not in product_links:
        product_links.append('https://in.puma.com/' + link['href'])

with open('puma_manchester_city1.csv', 'w') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(['Product Name', 'Price', 'Description', 'Link'])

    for product_url in product_links:
        product_page = requests.get(product_url, headers=get_u_a())
        product_soup = BeautifulSoup(product_page.content, 'html.parser')
        product_name = product_soup.find('h1', class_='product-name').text.strip()
        price = clean_price(product_soup.find('span', class_='value').text)
        product_description = clean_description(product_soup.find('div', class_='content', itemprop="description").text)
        writer.writerow([product_name, price, product_description, product_url])
        print(product_name)
        print(get_u_a())
        time_delay()
