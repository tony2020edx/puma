import requests
from bs4 import BeautifulSoup
import pandas as pd
from lxml import etree as et
import sys
import time
import random

header = header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36",
    'Accept': '*/*', 'Accept-Encoding': 'gzip, deflate, br', 'Accept-Language': 'en-GB,en-US;q=0.9,en;q=0.8'
}

start_url = "https://www.amazon.in/s?i=shoes&bbn=1983525031&rh=n%3A1983525031%2Cp_89%3ANike&dc&qid=1658383297&rnid=3837712031&ref=sr_pg_"

start_url_adidas = "https://www.amazon.in/s?k=adidas+basketball+shoes&i=shoes&bbn=1983525031&rh=n%3A1983525031%2Cp_89%3AAdidas&dc&qid=1658383117&rnid=3837712031&ref=sr_pg_"

listing_urls = []

for count in range(1,16):
    listing_url = start_url + str(count)
    listing_urls.append(listing_url)
    print(listing_url)

for count in range(1,7):
    listing_url_adidas = start_url_adidas + str(count)
    listing_urls.append(listing_url_adidas)
    print(listing_url_adidas)

#writing listing urls into a text file
with open('listing_urls.txt', 'w') as f:
    for item in listing_urls:
        f.write("%s\n" % item)
