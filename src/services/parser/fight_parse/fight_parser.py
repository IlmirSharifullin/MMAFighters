import datetime
import time
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
import requests
import json

from src.factories import get_repository

ua = UserAgent()

st_accept = "text/html"
st_useragent = ua.chrome
url_mma = "https://mma.metaratings.ru/persons/"

s_headers = {
    "Accept": st_accept,
    "User-Agent": st_useragent
}


def parse_fight_date(headers):
    all_fights = []
    for i in range(1, 2):

        url = f'https://mma.metaratings.ru/prognozy/?page={i}'
        if i == 1:
            url = 'https://mma.metaratings.ru/prognozy/'

        req = requests.get(url, headers)
        src = req.text
        soup = BeautifulSoup(src, 'lxml')

        list_of_fights = soup.find('div', class_='TipsList_TipsList__e7Ivz').find_all(
            class_='TipsList_TipsBox__oz5r6 tipsItem')

        print(list_of_fights)

        for fight in list_of_fights:
            fight_info = {
                            'first_fighter_id': 0,
                            'second_fighter_id': 0,
                            'date': datetime.datetime.strptime(fight.find('time').get('datetime'), '%Y-%m-%d %H:%M'),
                            'place': ''
                          }

            fight_url = 'https://mma.metaratings.ru' + fight.find('a').get('href')
            req = requests.get(fight_url, headers)
            src = req.text
            soup = BeautifulSoup(src, 'lxml')

            all_fights.append(fight_info)

    print(all_fights)



