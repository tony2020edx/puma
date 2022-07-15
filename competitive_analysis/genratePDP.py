import requests
from bs4 import BeautifulSoup
import csv
from lxml import etree
import time
import random


def time_delay():  # code to add a time delay between requests
    list1 = [2.8, 3.1, 3.6, 4, 4.5, 5.5, 6]
    x = random.choice(list1)
    time.sleep(x)


def cleanup_sale_price(price):
    price = price.replace("₹", "")
    price = price.replace(",", "")

    return price


def clean_mrp(price):
    price = price.replace(",", "")

    return price


def cleanup_discount(discount_string):
    discount_string = discount_string.replace("off", "")
    discount_string = ''.join(filter(str.isalnum, discount_string))

    return discount_string


def get_ratings(text):
    text_list = text.split(" ")
    if len(text_list) == 5:
        rating_value = text_list[0]
    elif len(text_list) == 3:
        rating_value = text_list[0]
    else:
        rating_value = 0

    return rating_value


def get_reviews(text):
    text_list = text.split(" ")
    if len(text_list) == 5:
        review_value = text_list[3]
    elif len(text_list) == 3:
        review_value = 0
    else:
        review_value = 0

    return review_value


header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36"
    , "Accept": '*/*',
    "Accept-Encoding": "gzip, deflate, br",
    "Connection": "keep-alive",
}

all_home_urls = []

base_url_puma = "https://www.flipkart.com/search?q=running+shoes+for+men&sid=osp%2Ccil%2C1cu&as=on&as-show=on&otracker=AS_QueryStore_OrganicAutoSuggest_1_13_na_na_na&otracker1=AS_QueryStore_OrganicAutoSuggest_1_13_na_na_na&as-pos=1&as-type=RECENT&suggestionId=running+shoes+for+men%7CSports+Shoes&requestId=4922c884-a369-4627-9d44-a1c96daba1be&as-searchtext=running+shoes&p%5B%5D=facets.size_uk%255B%255D%3D10&p%5B%5D=facets.brand%255B%255D%3DPUMA&page="
base_url_adidas = "https://www.flipkart.com/search?q=running+shoes+for+men&sid=osp%2Ccil%2C1cu&as=on&as-show=on&otracker=AS_QueryStore_OrganicAutoSuggest_1_13_na_na_na&otracker1=AS_QueryStore_OrganicAutoSuggest_1_13_na_na_na&as-pos=1&as-type=RECENT&suggestionId=running+shoes+for+men%7CSports+Shoes&requestId=4922c884-a369-4627-9d44-a1c96daba1be&as-searchtext=running+shoes&p%5B%5D=facets.size_uk%255B%255D%3D10&p%5B%5D=facets.brand%255B%255D%3DADIDAS&page="
base_url_nike = "https://www.flipkart.com/search?q=running+shoes+for+men&sid=osp%2Ccil%2C1cu&as=on&as-show=on&otracker=AS_QueryStore_OrganicAutoSuggest_1_13_na_na_na&otracker1=AS_QueryStore_OrganicAutoSuggest_1_13_na_na_na&as-pos=1&as-type=RECENT&suggestionId=running+shoes+for+men%7CSports+Shoes&requestId=4922c884-a369-4627-9d44-a1c96daba1be&as-searchtext=running+shoes&p%5B%5D=facets.size_uk%255B%255D%3D10&p%5B%5D=facets.brand%255B%255D%3DNIKE&page="
base_url_sketchers = "https://www.flipkart.com/search?q=running+shoes+for+men&sid=osp%2Ccil%2C1cu&as=on&as-show=on&otracker=AS_QueryStore_OrganicAutoSuggest_1_13_na_na_na&otracker1=AS_QueryStore_OrganicAutoSuggest_1_13_na_na_na&as-pos=1&as-type=RECENT&suggestionId=running+shoes+for+men%7CSports+Shoes&requestId=4922c884-a369-4627-9d44-a1c96daba1be&as-searchtext=running+shoes&p%5B%5D=facets.size_uk%255B%255D%3D10&p%5B%5D=facets.brand%255B%255D%3DSkechers&page="

for i in range(1, 21):
    url = base_url_puma + str(i)
    all_home_urls.append(url)
    print("Puma completed")

for i in range(1, 17):
    url = base_url_adidas + str(i)
    all_home_urls.append(url)
    print("Adidas completed")

for i in range(1, 5):
    url = base_url_nike + str(i)
    all_home_urls.append(url)
    print("Nike completed")

for i in range(1, 3):
    url = base_url_sketchers + str(i)
    all_home_urls.append(url)
    print("Sketchers completed")

print(len(all_home_urls))
print("Home url generation complete")

pdp_urls = []

def get_pdp(home_link):

    response = requests.get(home_link, headers=header)

    if response.status_code == 200:

        print("PDP generation started for {}".format(url))
        soup = BeautifulSoup(response.content, 'html.parser')
        dom = etree.HTML(str(soup))

        pdp_url_object = dom.xpath('//a[@class="_2UzuFa"]/@href')

        for pdp_url in pdp_url_object:
            pdp_urls.append("https://www.flipkart.com" + pdp_url)
            time_delay()





for url in all_home_urls:



    count = len(pdp_urls)





