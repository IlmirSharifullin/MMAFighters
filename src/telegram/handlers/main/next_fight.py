from aiogram import Router, Bot, F
from aiogram.types import CallbackQuery, Message

from src.services.database import Repository, DBFight
from src.telegram.callback_data import FighterCallbackData
from src.telegram.handlers.main.get_fighter_card import get_fighter_card
from src.telegram.keyboards.inline_fighters import get_fight_info_keyboards

router = Router(name='next_fight')


@router.message(F.text == 'Следующий бой')
async def select_data(message: Message, repository: Repository):
    fight: DBFight = await repository.fight.get_next()
    text = f'{fight.first_fighter.name} vs {fight.second_fighter.name}\n'
    text += f'Дата проведения - {fight.date}\n'
    text += f'Место проведения - {fight.place}'
    kb = get_fight_info_keyboards(first_fighter_id=fight.first_fighter_id, second_fighter_id=fight.second_fighter_id,
                                  first_fighter_name=fight.first_fighter.name, second_fighter_name=fight.second_fighter.name)
    await message.answer(text,
                         reply_markup=kb)


@router.callback_query(FighterCallbackData.filter())
async def get_fighter_query(query: CallbackQuery, callback_data: FighterCallbackData, repository: Repository):
    fighter = await repository.fighter.get(callback_data.fighter_id)
    text = get_fighter_card(fighter)
    await query.message.answer(text)
    await query.answer()
