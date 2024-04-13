from src.factories import get_repository, get_bot
from src.parser.fight_parse.fight_parser import parse_fight_date
from src.services.database import DBUser, DBFight
from .notifications import send_message


async def daily_fight_parser():
    repository = get_repository()
    bot = get_bot()
    new_fights = await parse_fight_date(1, 1)

    users: list[DBUser] = await repository.user.get_all()
    for fight in new_fights:
        for user in users:
            # if fight in user.favorites:
            #
            text = get_fight_card(fight)
            kb = None
            error = await send_message(bot, user.chat_id, text, kb, None)


def get_fight_card(fight: DBFight) -> str:
    return f'''Новый бой!'''
