import requests
from bs4 import BeautifulSoup
import pandas as pd
from lxml import etree as et
import sys
import time
import random

header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36",
    'Accept': '*/*', 'Accept-Encoding': 'gzip, deflate, br', 'Accept-Language': 'en-GB,en-US;q=0.9,en;q=0.8'
}

product_page_urls = []


def get_product_page_urls(target_dom):
    try:
        product_page_url = target_dom.xpath('//h2[@class="a-size-mini a-spacing-none a-color-base s-line-clamp-2"]/a/@href')

        for item in product_page_url:
            if item not in product_page_urls:
                final_url = "https://www.amazon.in" + item
                final_url = final_url.split("ref")[0]
                product_page_urls.append(final_url)


    except Exception as e:
        print(e)
        pass

#open the text file containing the listing urls
with open('listing_urls.txt', 'r') as f:
    for line in f:
        url = line.strip()
        response = requests.get(url, headers=header)
        soup = BeautifulSoup(response.content, 'html.parser')
        dom = et.HTML(str(soup))
        get_product_page_urls(dom)
        time.sleep(random.randint(1, 20))

        print(url)

#write product page urls into a text file

with open('product_page_urls.txt', 'w') as f:
    for item in product_page_urls:
        f.write("%s\n" % item)
        print(item)

print(len(product_page_urls))