import requests
from bs4 import BeautifulSoup
from lxml import etree
import time
import random

url = ["https://www.nike.com/in/w/new-lifestyle-shoes-13jrmz3n82yzy7ok",
       "https://www.nike.com/in/w/new-mens-lifestyle-shoes-13jrmz3n82yznik1zy7ok",
       "https://www.nike.com/in/w/new-mens-black-lifestyle-shoes-13jrmz3n82yz90poyznik1zy7ok",
       "https://www.nike.com/in/w/new-mens-white-lifestyle-shoes-13jrmz3n82yz4g797znik1zy7ok",
       "https://www.nike.com/in/w/new-mens-lifestyle-shoes-13jrmz1n3adz3abn9z3n82yz416lqz557pqz6s5r5z8hfx3za6d74zayp69zbdkaznik1zy7ok",
       "https://www.nike.com/in/w/new-jordan-shoes-37eefz3n82yzy7ok",
       "https://www.nike.com/in/w/new-black-running-shoes-37v7jz3n82yz90poyzy7ok",
       "https://www.nike.com/in/w/new-white-running-shoes-37v7jz3n82yz4g797zy7ok",
       "https://www.nike.com/in/w/new-mens-running-shoes-37v7jz3n82yznik1zy7ok",
       "https://www.nike.com/in/w/new-womens-running-shoes-37v7jz3n82yz5e1x6zy7ok",
       ]

user_agent_list = [
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36',
    'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.71 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/11.1.2 Safari/605.1.15',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_6_8) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.112 Safari/537.36'
]

product_urls = []


def time_delay():  # code to add a time delay between requests
    list1 = [1, 2, 2.6, 2.8, 3.1, 3.6, 4, 4.5, 5.5, 6]
    x = random.choice(list1)
    time.sleep(x)


def get_u_a():  # get a random user agent
    user_agent = random.choice(user_agent_list)
    headers = {'User-Agent': user_agent}

    return headers


def get_pdp_urls(base_url):
    web_page = requests.get(base_url, headers=get_u_a())
    soup = BeautifulSoup(web_page.content, 'html.parser')

    dom = etree.HTML(str(soup))

    product_link = (dom.xpath('//a[@class="product-card__link-overlay"]/@href'))

    for i in product_link:
        if i not in product_urls:
            product_urls.append(i)

    return product_urls


for home_links in url:
    get_pdp_urls(home_links)
    time_delay()

for i in product_urls:
    print(i)
    print("\n")


