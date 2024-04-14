import asyncio
import logging
import sys

from aiogram import Dispatcher, Bot
from apscheduler.schedulers.asyncio import AsyncIOScheduler

from src.middlewares.outer.database import DBSessionMiddleware
from src.services.database import create_pool
from src.settings import Settings
from dotenv import load_dotenv
from src.telegram.handlers.main import card_of_figfters, next_fight, forecast, start
from src.scheduler.daily_fight_parser import daily_fight_parser
load_dotenv()


async def main():
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s - %(levelname)s - %(name)s- %(message)s')
    settings: Settings = Settings()

    dp = Dispatcher()
    bot = Bot(token=settings.bot_token.get_secret_value())
    pool = create_pool(
        dsn=settings.build_postgres_dsn())
    dp.update.outer_middleware(DBSessionMiddleware(session_pool=pool))
    dp.include_routers(start.router,card_of_figfters.router, next_fight.router,forecast.router)

    scheduler = AsyncIOScheduler()
    scheduler.add_job(daily_fight_parser, trigger='cron', hour='12')
    scheduler.start()

    await dp.start_polling(bot)


if __name__ == '__main__':
    if sys.platform == "win32":
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    asyncio.run(main())
