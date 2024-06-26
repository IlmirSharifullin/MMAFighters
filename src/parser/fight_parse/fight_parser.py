import asyncio
import datetime
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
import requests
import re
import sys

from src.factories import get_repository
from src.services.database import DBFight

ua = UserAgent()

st_accept = "text/html"
st_useragent = ua.chrome
url_mma = "https://mma.metaratings.ru/persons/"

headers = {
    "Accept": st_accept,
    "User-Agent": st_useragent
}


async def parse_fight_date(left, right) -> list[DBFight]:
    new_fights = []
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
                    fight_place = ''
                    if info_split[j + 1] != info_split[-1]:
                        fight_place = info_split[j + 1]

                    repository = get_repository()

                    first_fighter = await repository.fighter.get_by_name(first_fighter_name)
                    second_fighter = await repository.fighter.get_by_name(second_fighter_name)

                    if first_fighter is None or second_fighter is None:
                        break

                    fight, is_new = await repository.fight.create(first_fighter=first_fighter,
                                                                  second_fighter=second_fighter,
                                                                  date=fight_date, place=fight_place)
                    if is_new:
                        new_fights.append(fight)
                    break

    return new_fights


if sys.platform == "win32":
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
