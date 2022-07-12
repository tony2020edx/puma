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
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36",
    "accept-encoding": "gzip, deflate, br",
    "Connection": "keep-alive",
}

home_urls = []







product_links = ["https://www.flipkart.com/skechers-tr-ultra-casuals-men/p/itm6e17c7f91f135?pid=SHOGFFJT7EUFHZAW&"]


with open("sneaker_pdp.csv", "w") as csv_file:
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow(['Product Url','Product Name', 'Brand', 'Sale Price', 'MRP', 'Seller Rating', 'Ratings Count', 'Reviews Count', 'Discount', 'Product Rating'])

    for product_url in product_links:

        pdp_response = requests.get(product_url, headers=header)
        soup = BeautifulSoup(pdp_response.content, 'html.parser')
        dom = etree.HTML(str(soup))

        try:
            product_name = dom.xpath('//span[@class="B_NuCI"]/text()')[0]
        except Exception as e:
            product_name = "NA"

        try:
            brand_name = dom.xpath('//span[@class="G6XhRU"]/text()')[0]
        except Exception as e:
            brand_name = "NA"

        try:
            sale_price = dom.xpath('//div[@class="_30jeq3 _16Jk6d"]/text()')[0]
            sale_price = cleanup_sale_price(sale_price)
        except Exception as e:
            sale_price = 0

        try:
            mrp = dom.xpath('//div[@class="_3I9_wc _2p6lqe"]/text()')[1]
            mrp = clean_mrp(mrp)
        except Exception as e:
            mrp = 0

        try:
            seller_rating = dom.xpath('//div[@class="_3LWZlK _1D-8OL"]/text()')[0]
        except Exception as e:
            seller_rating = 0

        try:
            ratings_and_reviews = dom.xpath('//span[@class="_2_R_DZ"]/span/text()')
            ratings = get_ratings(ratings_and_reviews[0])
            reviews = get_reviews(ratings_and_reviews[0])
        except Exception as e:
            ratings = 0
            reviews = 0

        try:
            discount = cleanup_discount(dom.xpath('//div[@class="_3Ay6Sb _31Dcoz pZkvcx"]/span/text()')[0])

        except Exception as e:
            discount = 0

        try:
            product_rating = dom.xpath('//div[@class="_3LWZlK _3uSWvT"]/text()')[0]
        except Exception as e:
            product_rating = 0

        csv_writer.writerow([product_url,product_name, brand_name, sale_price, mrp, seller_rating, ratings, reviews, discount, product_rating])
        print(product_url,product_name, brand_name, sale_price, mrp, seller_rating, ratings, reviews, discount, product_rating)







