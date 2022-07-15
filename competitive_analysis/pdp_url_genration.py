import requests
from bs4 import BeautifulSoup
import csv
from lxml import etree
import time
import random

header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36"}

def time_delay():  # code to add a time delay between requests
    list1 = [2.8, 3.1, 3.6, 4, 4.5, 5.5, 6]
    x = random.choice(list1)
    time.sleep(x)


home_links = []

with open('urls.txt', 'r') as f:
    for line in f:
        home_link = line.strip()
        home_links.append(home_link)

pdp_urls = []

for url in home_links:

    url = url.replace("\n", "")

    response = requests.get(url, headers=header)

    if response.status_code == 200:

        print("PDP generation started for {}".format(home_link))
        soup = BeautifulSoup(response.content, 'html.parser')
        dom = etree.HTML(str(soup))

        pdp_url_object = dom.xpath('//a[@class="_2UzuFa"]/@href')

        for pdp_url in pdp_url_object:
            pdp_urls.append("https://www.flipkart.com" + pdp_url)
            time_delay()



print(len(pdp_urls))


for i in pdp_urls:
    print(i)
    print("\n")

print(len(pdp_urls))

with open('pdp_urls.txt' , 'w') as f:
    for i in pdp_urls:
        f.write(i + "\n")
        print("PDP url written to file")


