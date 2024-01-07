import requests
import json
from bs4 import BeautifulSoup


def get_top():
    url = 'https://www.kinopoisk.ru/lists/movies/top250/'
    response = requests.get(url)
    print(response.text)
    soup = BeautifulSoup(response.text, 'lxml')
    res = soup.body.find_all('script', class_='__NEXT_DATA__')
    print(res)


if __name__ == '__main__':
    get_top()
