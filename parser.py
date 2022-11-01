import requests
from bs4 import BeautifulSoup as bs
import csv


i = 0
url= 'https://www.kinoafisha.info/rating/movies/'


def csv_read(data):
    with open('data.csv', 'a') as file:
        writer = csv.writer(file, lineterminator = '\r')
        writer.writerow((data['film'], data['year'], data['rate'], data['genre'], data['image'], data['href_']))


while i<=19:
    url_n = url + f'?page={i}'
    req = requests.get(url_n)
    soupy = bs(req.text, 'html.parser')
    for f in range(100):
        film = soupy.find_all('a', class_='movieItem_title')[f].text
        rate = soupy.find_all('span', class_='rating_num')[f].text
        genre = soupy.find_all('span', class_='movieItem_genres')[f].text
        year = soupy.find_all('span', class_='movieItem_year')[f].text.split(',')[0]
        image = soupy.find_all('picture', class_='movieItem_poster picture picture-poster')[f].find('img', class_='picture_image').get('data-picture')
        href_ = soupy.find_all('a', class_='movieItem_title')[f].get('href')
        data = {'film': film, 'year': year, 'rate': rate, 'genre': genre, 'image': image, 'href_': href_}
        csv_read(data)
        print(film, year, rate, genre, href_)
    i+=1

