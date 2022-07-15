# a web scraper to scrape the IMDB website for movies and their ratings and more

import requests
from bs4 import BeautifulSoup
from lxml import etree as et

header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36"}

start_url = "https://www.imdb.com/chart/top"

movie_urls = []

count = 0

with open("movie_urls.txt", "r") as f:
    for line in f:
        movie_urls.append(line.strip())

for movie_url in movie_urls:
    movie_response = requests.get(movie_url, headers=header)
    movie_soup = BeautifulSoup(movie_response.content, 'html.parser')
    movie_dom = et.HTML(str(movie_soup))

    movie_name = movie_dom.xpath('//h1[@data-testid="hero-title-block__title"]/text()')[0]
    global_rank = count + 1
    count += 1

    genre = movie_dom.xpath('//span[@class="ipc-chip__text"]/text()')[0]

    director_name = movie_dom.xpath('//a[@class="ipc-metadata-list-item__list-content-item ipc-metadata-list-item__list-content-item--link"]/text()')[0]

    rating = movie_dom.xpath('//span[@class="sc-7ab21ed2-1 jGRxWM"]/text()')[0]

    actors_list = movie_dom.xpath('//a[@data-testid="title-cast-item__actor"]/text()')
