
import requests
from bs4 import BeautifulSoup
from lxml import etree as et
import time
import random
import json
from unidecode import unidecode

header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36"}

#listing_page = "https://www.redfin.com//CA/San-Francisco/43-Green-St-94123/apartment/177598754"
listing_page = "https://www.redfin.com/CA/Emeryville/6301-Shellmound-St-94608/home/143116529"

listing_page_response = requests.get(listing_page, headers=header)
listing_page_soup = BeautifulSoup(listing_page_response.content, 'html.parser')
listing_page_dom = et.HTML(str(listing_page_soup))

address = listing_page_dom.xpath('//div[@class="homeAddress"]//text()')
address = " ".join(address)


price = listing_page_dom.xpath('//div[@class="statsValue"]//text()')[0]
print(price)

