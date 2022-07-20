from ast import Try
from bs4 import BeautifulSoup
import requests
from csv import writer
import time
import random
from lxml import etree as et

header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.66 Safari/537.36"}

base_url = "https://www.pararius.com/apartment-for-rent/amsterdam/737a2b99/beethovenstraat"



def time_delay():
    time.sleep(random.randint(2, 5))


response = requests.get(base_url, headers=header)

soup = BeautifulSoup(response.content, 'html.parser')
dom = et.HTML(str(soup))

price = dom.xpath('//div[@class="listing-detail-summary__price"]/text()')
print(price)

text = ['\n                €2,700\n\n                                    ', '\n']
