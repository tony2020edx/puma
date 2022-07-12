import requests
from bs4 import BeautifulSoup
from lxml import etree

url = "https://www.formula1.com/"

web_page = requests.get(url)
soup = BeautifulSoup(web_page.content, 'html.parser')

dom = etree.HTML(str(soup))
result = (dom.xpath('//p[@class="f1--s no-margin"]/text()'))
news_link = (dom.xpath('//a/@href'))



for i in news_link:
    if "article" in i:
        print("https://www.formula1.com"+i)
        print("\n")


