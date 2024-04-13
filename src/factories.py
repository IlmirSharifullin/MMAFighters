import asyncio
import datetime

from aiogram import Bot
from dotenv import load_dotenv

from src.services.database import Repository, create_pool
from src.settings import Settings

load_dotenv()


def get_repository() -> Repository:
    settings: Settings = Settings()
    dsn = settings.build_postgres_dsn()
    # print(dsn)
    pool = create_pool(dsn=dsn)
    repository = Repository(session=pool())
    return repository


def get_bot() -> Bot:
    settings: Settings = Settings()

    bot = Bot(settings.bot_token.get_secret_value())
    return bot


async def test():
    repo = get_repository()
    randomized = await repo.fight.get_next()
    print(randomized)
