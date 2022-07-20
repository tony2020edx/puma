import requests
from bs4 import BeautifulSoup
from lxml import etree as et
import pandas as pd
from twilio.rest import Client

header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36",
    'Accept': '*/*', 'Accept-Encoding': 'gzip, deflate, br', 'Accept-Language': 'en-GB,en-US;q=0.9,en;q=0.8'
}

amazon_urls = ['https://www.amazon.in/Garmin-010-02064-00-Instinct-Monitoring-Graphite/dp/B07HYX9P88/',
               'https://www.amazon.in/Rockerz-370-Headphone-Bluetooth-Lightweight/dp/B0856HRTJG/',
               'https://www.amazon.in/Logitech-MK215-Wireless-Keyboard-Mouse/dp/B012MQS060/',
               'https://www.amazon.in/Logitech-G512-Mechanical-Keyboard-Black/dp/B07BVCSRXL/',
               'https://www.amazon.in/BenQ-inch-Bezel-Monitor-Built/dp/B073NTCT4R/'
               ]


def get_amazon_price(dom):
    item_price = dom.xpath('//span[@class="a-offscreen"]/text()')[0]
    item_price = item_price.replace(',', '').replace('₹', '').replace('.00', '')
    return int(item_price)


def get_product_name(dom):
    name = dom.xpath('//span[@id="productTitle"]/text()')
    [name.strip() for name in name]
    return name[0]


def get_master_price(url):
    for row in df.itertuples():
        if row.url == url:
            return row.price
    return None


price_drop_list = []
price_drop_list_url = []

for product_url in amazon_urls:

    response = requests.get(product_url, headers=header)
    soup = BeautifulSoup(response.content, 'html.parser')
    main_dom = et.HTML(str(soup))

    price = get_amazon_price(main_dom)
    product_name = get_product_name(main_dom)
    df = pd.read_csv('new_master_Data.csv')

    if price < get_master_price(product_url):
        change_percentage = round((get_master_price(product_url) - price) * 100 / get_master_price(product_url))
        print(' There is a {}'.format(change_percentage), '% drop in price for {}'.format(product_name))
        print('Click here to purchase {}'.format(product_url))

        price_drop_list.append(product_name)
        price_drop_list_url.append(product_url)

messege = "There is a drop in price for {}".format(len(price_drop_list)) + " products." + "Click to purchase"

for items in price_drop_list_url:
    messege = messege + "\n" + items

account_sid = 'ACfeb15a884ed55d7f9d6ef5b803fdd811'
auth_token = '54e681e9436133f2f5ac46a4ada30a86'

client = Client(account_sid, auth_token)
message = client.messages.create(
    from_='+19707071122',
    body=messege,
    to='+919605703702'
)

print(message.sid)
print(message.body)
