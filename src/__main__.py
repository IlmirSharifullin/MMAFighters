import asyncio

from aiogram import Dispatcher, Bot, F

from src.settings import Settings
from dotenv import load_dotenv
from src.telegram.handlers.main import card_of_figfters, next_fight, past_fight, forecast, start

load_dotenv()


async def main():
    settings: Settings = Settings()

    dp = Dispatcher()
    bot = Bot(token=settings.bot_token.get_secret_value())

    dp.include_routers(start.router,card_of_figfters.router, next_fight.router, past_fight.router,forecast.router)
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())