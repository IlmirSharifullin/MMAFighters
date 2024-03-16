import asyncio
import datetime

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


async def test():
    repo = get_repository()
    fighters = await repo.fighter.get_all()
    two = fighters[:2]
    fight = await repo.fight.create(two[0], two[1], datetime.datetime.now(), 'Moscow Arena')
    print(fight)
