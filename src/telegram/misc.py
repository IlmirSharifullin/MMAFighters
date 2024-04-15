from aiogram import F, Router
from aiogram.types import Message

from src.services.database import Repository, DBFight
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