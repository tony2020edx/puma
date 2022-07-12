import requests
from bs4 import BeautifulSoup
import csv
from lxml import etree
import time
import random



def time_delay():  # code to add a time delay between requests
    list1 = [1, 2, 2.6, 2.8, 3.1, 3.6, 4, 4.5, 5.5, 6]
    x = random.choice(list1)
    time.sleep(x)



base_url ="https://www.flipkart.com/search?q=sneakers&as=on&as-show=on&otracker=AS_Query_OrganicAutoSuggest_3_4_na_na_na&otracker1=AS_Query_OrganicAutoSuggest_3_4_na_na_na&as-pos=3&as-type=RECENT&suggestionId=sneakers&requestId=9959ff5e-69ce-43dc-87d5-8c238ce8c98b&as-searchtext=snea&p%5B%5D=facets.brand%255B%255D%3DSkechers"


header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36" ,
    "accept-encoding": "gzip, deflate, br",
    "Connection": "keep-alive",
           }

pdp_urls = []

def get_pdp_urls(url):
    response = requests.get(url, headers=header)
    soup = BeautifulSoup(response.content, 'html.parser')
    dom = etree.HTML(str(soup))

    pdp_url_object = dom.xpath('//a[@class="_2UzuFa"]/@href')

    for pdp_url in pdp_url_object:
        pdp_urls.append("https://www.flipkart.com" + pdp_url)


