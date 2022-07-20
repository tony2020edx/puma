#scrape data from redfin

import requests
from bs4 import BeautifulSoup
from lxml import etree as et
import time
import random
import json
from unidecode import unidecode


header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36"}
url = "https://www.redfin.com/city/17151/CA/San-Francisco/apartments-for-rent"

listing_page_list = ["https://www.redfin.com/city/17151/CA/San-Francisco/apartments-for-rent/filter/property-type=multifamily"]

property_links = []

listing_page_url = "https://www.redfin.com/city/17151/CA/San-Francisco/apartments-for-rent/filter/property-type=multifamily/page-"

for i in range(1, 10):
    listing_page = listing_page_url + str(i)
    listing_page_list.append(listing_page)


def get_property_url(url):
    response = requests.get(url, headers=header)
    soup = BeautifulSoup(response.content, 'html.parser')
    dom = et.HTML(str(soup))

    property_link_list = dom.xpath('//div[@class="link-and-anchor"]/../@href')

    for link in property_link_list:
        property_links.append("https://www.redfin.com/" + link)

    print("processed {} pages".format(url))

for listing_page_url in listing_page_list:
    get_property_url(listing_page_url)
    time.sleep(random.randint(1, 5))

#write property links to a a text file

with open("property_links.txt", "w") as f:
    for link in property_links:
        f.write(link + "\n")

