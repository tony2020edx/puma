#a web scraper to scrape the IMDB website for movies and their ratings and more

import requests
from bs4 import BeautifulSoup
from lxml import etree as et
import csv
import time
import random

header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36"}

def time_delay():  # code to add a time delay between requests
    list1 = [2.8, 3.1, 3.6, 4, 4.5, 5.5, 6]
    x = random.choice(list1)
    time.sleep(x)



start_url ="https://www.imdb.com/chart/top"

movie_urls = []

response = requests.get(start_url, headers=header)
soup = BeautifulSoup(response.content, 'html.parser')
dom = et.HTML(str(soup))

movie_urls_list = dom.xpath('//td[@class="titleColumn"]/a/@href')

for i in movie_urls_list:
    short_url = "https://www.imdb.com" + i
    short_url = short_url.split("?")[0]
    movie_urls.append(short_url)

count = 0

#write data to a file called imdb_data.csv
with open("imdb_data.csv", "w") as f:
    writer = csv.writer(f)
    writer.writerow(["Movies Url", "Rank","Movie Year", "Movie Name", "Genre", "Director", "Rating", "Actors"])
    for movie_url in movie_urls:
        response = requests.get(movie_url, headers=header)
        soup = BeautifulSoup(response.content, 'html.parser')
        dom = et.HTML(str(soup))

        rank = count + 1
        movie_name = dom.xpath('//h1[@data-testid="hero-title-block__title"]/text()')[0]
        movie_year = dom.xpath('//a[@class="ipc-link ipc-link--baseAlt ipc-link--inherit-color sc-8c396aa2-1 WIUyh"]/text()')[0]
        genre = dom.xpath('//span[@class="ipc-chip__text"]/text()')
        director_name = dom.xpath('//a[@class="ipc-metadata-list-item__list-content-item ipc-metadata-list-item__list-content-item--link"]/text()')[0]
        rating = dom.xpath('//span[@class="sc-7ab21ed2-1 jGRxWM"]/text()')[0]
        actors_list = dom.xpath('//a[@data-testid="title-cast-item__actor"]/text()')

        writer.writerow([movie_url,rank, movie_year,movie_name, genre, director_name, rating, actors_list])

        print(movie_name, genre, director_name, rating, actors_list, movie_year)
        count += 1
        print("\n")
        print(count)
        time_delay()

