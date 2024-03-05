import asyncio
import sys
from src.factories import get_repository
from src.services.parser.fighter_info_parser import parse_all_info
import datetime
import time
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
import requests
import json

ua = UserAgent()

st_accept = "text/html"
st_useragent = ua.chrome
url_mma = "https://mma.metaratings.ru/persons/"

s_headers = {
    "Accept": st_accept,
    "User-Agent": st_useragent
}

if sys.platform == "win32":
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

asyncio.run(parse_all_info(headers=s_headers))

# for item in fighters:
#     print(item['Имя'])
#     repo.fighter.insert(name=item['Имя'], country=item['Страна'], base_style=item['Базовый стиль'],
#                         promotion=item['Промоушен'], city=item['Город'], age=item['Возраст'],
#                         date_of_birth=item['Дата рождения'], weight=item['Вес'], height=item['Рост'],
#                         weight_category=item['Вес. категория'], arm_span=item['Размах рук'],
#                         wins_count=item['Победы'], wins_knockouts_count=item['Нокаут_победы'],
#                         wins_submissions_count=item['Сабмишн_победы'],
#                         wins_judges_decisions_count=item['Суд_решения_победы'], defeats_count=item['Поражения'],
#                         defeats_knockouts_count=item['Нокаут_поражения'],
#                         defeats_submissions_count=item['Сабмишн_поражения'],
#                         defeats_judges_decisions_count=item['Суд_решения_поражения'])
