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

    randomized = await repo.fight.get_random_n(5)
    print(randomized)

