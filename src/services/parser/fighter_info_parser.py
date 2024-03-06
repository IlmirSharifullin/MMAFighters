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


async def parse_all_info(headers):
    with open('all_fighters_dict_2.json', encoding='utf-8') as file:
        all_fighters = json.load(file)

    # count = 0
    fighters = []
    for fighter_name, fighter_href in all_fighters.items():

        # count += 1
        # print(fighter_name, count)

        url = fighter_href
        req = requests.get(url, headers)
        src = req.text

        soup = BeautifulSoup(src, 'lxml')

        params_heads = soup.find_all(class_='Head_infoItemLeft__v1Gje')
        fighters_data = soup.find_all(class_='Head_infoItemRight__fqxnt')

        fighter_dict = {'Имя': fighter_name}
        fighter_dict['Страна'] = ''
        fighter_dict['Базовый стиль'] = ''
        fighter_dict['Промоушен'] = ''
        fighter_dict['Город'] = ''
        fighter_dict['Возраст'] = 0
        fighter_dict['Дата рождения'] = datetime.datetime.strptime('01.01.1900', '%d.%m.%Y')
        fighter_dict['Вес'] = 0
        fighter_dict['Рост'] = 0
        fighter_dict['Вес. категория'] = ''
        fighter_dict['Размах рук'] = 0

        for i in range(len(params_heads)):
            if params_heads[i].text == 'Возраст':
                fighter_dict[params_heads[i].text] = int(fighters_data[i].text.split(' ')[0])
                fighter_dict['Дата рождения'] = datetime.datetime.strptime(fighters_data[i].text.split()[2][1:-1],
                                                                           '%d.%m.%Y')
                continue

            if params_heads[i].text == 'Рост, вес':
                if '.' not in fighters_data[i].text.split(' ')[0]:
                    fighter_dict['Рост'] = int(fighters_data[i].text.split(' ')[0])
                else:
                    fighter_dict['Вес'] = int(fighters_data[i].text.split(' ')[0].split('.')[0])

                if '.' not in fighters_data[i].text.split(' ')[1][3:]:
                    fighter_dict['Вес'] = int(fighters_data[i].text.split(' ')[1][3:]) if fighters_data[i] != '' else (
                        fighters_data[i + 1].text.split(' ')[1][3:])
                else:
                    fighter_dict['Вес'] = int(fighters_data[i].text.split(' ')[1][3:].split('.')[0])

            if params_heads[i].text == 'Размах рук':
                fighter_dict[params_heads[i].text] = int(fighters_data[i].text.split(' ')[0])
                continue

            fighter_dict[params_heads[i].text] = fighters_data[i].text if fighters_data[i] != '' else fighters_data[
                i + 1].text

        fighter_dict['Победы'] = 0
        fighter_dict['Нокаут_победы'] = 0
        fighter_dict['Сабмишн_победы'] = 0
        fighter_dict['Суд_решения_победы'] = 0

        fighter_dict['Поражения'] = 0
        fighter_dict['Нокаут_поражения'] = 0
        fighter_dict['Сабмишн_поражения'] = 0
        fighter_dict['Суд_решения_поражения'] = 0

        wins_loses = soup.find_all(class_='Head_blockTotal__vdcMN')
        for item in wins_loses:
            name = item.text
            if 'Поб' in name:
                fighter_dict['Победы'] = name.split(' ')[0] if name.split(' ')[0] != '-' else 0

            if 'Пор' in name:
                fighter_dict['Поражения'] = name.split(' ')[0] if name.split(' ')[0] != '-' else 0

        w_l_stats = soup.find_all(class_='Head_blockTotal__vdcMN')
        if len(w_l_stats) > 0:
            w_stats = soup.find_all(class_='Head_blockTotal__vdcMN')[0].find_next_sibling()
            l_stats = soup.find_all(class_='Head_blockTotal__vdcMN')[1].find_next_sibling()
        else:
            w_stats = []
            l_stats = []

        for item in w_stats:
            name = item.text
            res = int(item.next_element.next_element.text)

            if 'Нокаут' in name:
                fighter_dict['Нокаут_победы'] = res

            elif 'Сабмишн' in name:
                fighter_dict['Сабмишн_победы'] = res

            elif 'Суд' in name:
                fighter_dict['Суд_решения_победы'] = res

        for item in l_stats:
            name = item.text
            res = int(item.next_element.next_element.text)

            if 'Нокаут' in name:
                fighter_dict['Нокаут_поражения'] = res

            elif 'Сабмишн' in name:
                fighter_dict['Сабмишн_поражения'] = res

            elif 'Суд' in name:
                fighter_dict['Суд_решения_поражения'] = res

        fighters.append(fighter_dict)
        time.sleep(1)
        repo = get_repository()

        await repo.fighter.insert(name=fighter_dict['Имя'], country=fighter_dict['Страна'],
                                  base_style=fighter_dict['Базовый стиль'],
                                  promotion=fighter_dict['Промоушен'], city=fighter_dict['Город'],
                                  age=fighter_dict['Возраст'],
                                  date_of_birth=fighter_dict['Дата рождения'], weight=fighter_dict['Вес'],
                                  height=fighter_dict['Рост'],
                                  weight_category=fighter_dict['Вес. категория'], arm_span=fighter_dict['Размах рук'],
                                  wins_count=fighter_dict['Победы'], wins_knockouts_count=fighter_dict['Нокаут_победы'],
                                  wins_submissions_count=fighter_dict['Сабмишн_победы'],
                                  wins_judges_decisions_count=fighter_dict['Суд_решения_победы'],
                                  defeats_count=fighter_dict['Поражения'],
                                  defeats_knockouts_count=fighter_dict['Нокаут_поражения'],
                                  defeats_submissions_count=fighter_dict['Сабмишн_поражения'],
                                  defeats_judges_decisions_count=fighter_dict['Суд_решения_поражения'])
