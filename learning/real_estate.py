import requests
from bs4 import BeautifulSoup
from lxml import etree as et
import time
import random
import json
from unidecode import unidecode

header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36"}



url = "https://www.pararius.com/apartment-for-rent/amsterdam/ed839c88/huidekoperstraat"

def page_date_extraction(url):
    response = requests.get(url, headers=header)
    soup = BeautifulSoup(response.content, 'html.parser')
    dom = et.HTML(str(soup))


    titile = dom.xpath('//h1[@class="listing-detail-summary__title"]/text()')[0]

    furnishing_status = dom.xpath('//li[@class="illustrated-features__item illustrated-features__item--interior"]/text()')[0]

    


print(titile)
print(furnishing_status)



