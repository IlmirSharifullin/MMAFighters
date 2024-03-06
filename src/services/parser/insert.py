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


def start_parse():
    asyncio.run(parse_all_info(headers=s_headers))
