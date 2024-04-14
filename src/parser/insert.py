import asyncio
import sys
from src.parser.fighter_parse.fighter_info_parser import parse_all_info
from fake_useragent import UserAgent

ua = UserAgent()

st_accept = "text/html"
st_useragent = ua.chrome
url_mma = "https://mma.metaratings.ru/persons/"

headers = {
    "Accept": st_accept,
    "User-Agent": st_useragent
}

if sys.platform == "win32":
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())


def start_parse():
    asyncio.run(parse_all_info())
