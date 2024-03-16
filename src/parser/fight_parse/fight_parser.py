import asyncio
import datetime
import time
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
import requests
import json
import re
import sys

from src.factories import get_repository

ua = UserAgent()

st_accept = "text/html"
st_useragent = ua.chrome
url_mma = "https://mma.metaratings.ru/persons/"

headers = {
    "Accept": st_accept,
    "User-Agent": st_useragent
}


async def parse_fight_date(left, right):
    for i in range(left, right + 1):

        url = f'https://mma.metaratings.ru/prognozy/?page={i}'
        if i == 1:
            url = 'https://mma.metaratings.ru/prognozy/'

        req = requests.get(url, headers)
        src = req.text
        soup = BeautifulSoup(src, 'lxml')

        list_of_fights = soup.find('div', class_='TipsList_TipsList__e7Ivz').find_all(
            class_='TipsList_TipsBox__oz5r6 tipsItem')

        for fight in list_of_fights:

            fight_date = datetime.datetime.strptime(fight.find('time').get('datetime'), '%Y-%m-%d %H:%M')
            fight_url = 'https://mma.metaratings.ru' + fight.find('a').get('href')

            req = requests.get(fight_url, headers)
            src = req.text
            soup = BeautifulSoup(src, 'lxml')

            information = str(soup.find(class_='versus-info workarea-text').find('div'))
            info_split = information.split('<br/>')
            for j in range(len(info_split)):
                if re.search("[А-я’Ёё]*[ -]*[А-я’Ёё]*[ -]*[А-я’Ёё]* [(][А-я’Ёё]*[)] – [А-я’Ёё]*[ -]*[А-я’Ёё]*[ -]*["
                             "А-я’Ёё]* [(][А-я’Ёё]*[)]", info_split[j]):
                    fighters_names = re.findall("[А-я’Ёё][ -]*[А-я’Ёё]*[ -]*[А-я’Ёё]* ", info_split[j])
                    first_fighter_name = fighters_names[0][:-1] if fighters_names[0] else ''
                    second_fighter_name = fighters_names[1][:-1] if fighters_names[1] else ''
                    place = ''
                    if info_split[j + 1] != info_split[-1]:
                        place = info_split[j + 1]

                    repository = get_repository()
                    f_fighter = await repository.fighter.get_by_name(first_fighter_name)
                    s_fighter = await repository.fighter.get_by_name(second_fighter_name)

                    if f_fighter is None or s_fighter is None:
                        print(first_fighter_name)
                        break

                    fight = await repository.fight.create(first_fighter=f_fighter, second_fighter=s_fighter,
                                                          date=fight_date, place=place)

                    print(f_fighter, s_fighter)
                    print(fight)

                    break


if sys.platform == "win32":
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
