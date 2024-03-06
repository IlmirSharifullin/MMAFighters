from bs4 import BeautifulSoup
from fake_useragent import UserAgent
import requests
import json


ua = UserAgent()

st_accept = "text/html"
st_useragent = ua.chrome
url_mma = "https://mma.metaratings.ru/persons/"

Us_headers = {
    "Accept": st_accept,
    "User-Agent": st_useragent
}


def pars_fighter_hrefs(url, headers):
    # create and filling .html file with main page
    req = requests.get(url, headers)
    src = req.text
    with open("index.html", 'w', encoding="utf-8") as file:
        file.write(src)

    with open("index.html", encoding="utf-8") as file:
        src = file.read()

    # parsing names and links to fighters pages
    soup = BeautifulSoup(src, 'lxml')
    all_fighters_hrefs = []
    all_fighters_hrefs += soup.find_all(class_="ArticlesList_articlesItemTitle__a5yze")[:21]

    for i in range(2, 51):
        url = f"https://mma.metaratings.ru/persons/?page={i}"
        req = requests.get(url, headers)
        src = req.text
        soup = BeautifulSoup(src, 'lxml')
        all_fighters_hrefs += soup.find_all(class_="ArticlesList_articlesItemTitle__a5yze")[:21]

    all_fighters = {}

    for item in all_fighters_hrefs:
        item_text = item.text
        item_href = 'https://mma.metaratings.ru/' + item.get('href')
        all_fighters[item_text] = item_href

    # create and filling .json file with names and links to fighters pages
    with open('all_fighters_dict_2.json', 'w', encoding='utf-8') as file:
        json.dump(all_fighters, file, indent=4, ensure_ascii=False)



