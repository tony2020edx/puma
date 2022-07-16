import requests
from bs4 import BeautifulSoup
from lxml import etree as et
import time
import random
import json
from unidecode import unidecode


def time_delay():
    time.sleep(random.randint(2, 5))


start_url = "https://www.imdb.com/chart/top"
header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36"}
movie_urls = []

response = requests.get(start_url, headers=header)
soup = BeautifulSoup(response.content, 'html.parser')
dom = et.HTML(str(soup))
movie_urls_list = dom.xpath('//td[@class="titleColumn"]/a/@href')

for i in movie_urls_list:
    long_url = "https://www.imdb.com" + i
    short_url = long_url.split("?")[0]
    movie_urls.append(short_url)

# write data into a json file

with open("data_v1.json", "w") as f:
    json.dump([], f)


def write_to_json(new_data, filename='data_v1.json'):
    with open(filename, 'r+') as file:
        file_data = json.load(file)
        file_data.append(new_data)
        file.seek(0)
        json.dump(file_data, file, indent=4)


for movie_url in movie_urls:
    response = requests.get(movie_url, headers=header)
    soup = BeautifulSoup(response.content, 'html.parser')
    dom = et.HTML(str(soup))

    rank = movie_urls.index(movie_url) + 1
    movie_name = dom.xpath('//h1[@data-testid="hero-title-block__title"]/text()')[0]
    movie_year = dom.xpath('//a[@class="ipc-link ipc-link--baseAlt ipc-link--inherit-color sc-8c396aa2-1 WIUyh"]/text()')[0]
    genre = dom.xpath('//span[@class="ipc-chip__text"]/text()')
    director_name = dom.xpath('//a[@class="ipc-metadata-list-item__list-content-item ipc-metadata-list-item__list-content-item--link"]/text()')[0]
    rating = dom.xpath('//span[@class="sc-7ab21ed2-1 jGRxWM"]/text()')[0]
    actors_list = dom.xpath('//a[@data-testid="title-cast-item__actor"]/text()')
    actors_list = [unidecode(i) for i in actors_list]

    write_to_json({'rank': rank,
                   'movie_name': movie_name,
                   'movie_url': movie_url,
                   'movie_year': movie_year,
                   'genre': genre,
                   'director_name': unidecode(director_name),
                   'rating': rating,
                   'actors': actors_list})

    time_delay()
    print("{} written to json file".format(rank))
