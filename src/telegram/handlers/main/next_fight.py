from aiogram import Router
from aiogram.types import CallbackQuery

from src.services.database import Repository
from src.telegram.callback_data import FighterCallbackData
from src.telegram.handlers.main.get_fighter_card import get_fighter_card


router = Router(name='next_fight')

@router.callback_query(FighterCallbackData.filter())
async def get_fighter_query(query: CallbackQuery, callback_data: FighterCallbackData, repository: Repository):
    fighter = await repository.fighter.get(callback_data.fighter_id)
    text = get_fighter_card(fighter)
    await query.message.answer(text)
    await query.answer()
