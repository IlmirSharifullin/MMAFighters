from aiogram import Router, Bot, F
from aiogram.types import CallbackQuery, Message

from src.services.database import Repository

router = Router(name='forecast')
@router.message(F.text=='Прогноз на следующий бой')
async def select_data(message: Message,repository: Repository ):
    answer = 'Прости, я пока не обладаю такой информацией'
    await message.answer(answer)