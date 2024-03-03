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
    print(await repo.fighter.insert('Ильмир', "Россия", "Самбо", "UFC", "Казань", 18, datetime.datetime.now(), 77, 185, "Средняя", 180, 5, 2, 2, 1, 1, 1, 0, 0))


asyncio.run(test())