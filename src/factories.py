import asyncio
import datetime

from dotenv import load_dotenv

from src.services.database import Repository, create_pool
from src.settings import Settings

load_dotenv()


def get_repository() -> Repository:
    settings: Settings = Settings()
    dsn = settings.build_postgres_dsn()
    pool = create_pool(dsn=dsn)
    repository = Repository(session=pool())
    return repository


async def test():
    repo = get_repository()
    fight = await repo.fight.get(2)

    test_unique = await repo.fight.create(fight.first_fighter, fight.second_fighter, fight.date, fight.place)

    print(fight)
    print(test_unique)
    print(fight == test_unique)

asyncio.run(test())