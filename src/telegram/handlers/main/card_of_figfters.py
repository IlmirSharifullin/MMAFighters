from aiogram import Router,  F
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from src.services.database import Repository, DBFighter
from src.telegram.states import FighterCardStates

router = Router(name='card_of_fighters')
@router.message(F.text=='Карточка бойца')
async def select_data(message: Message,repository: Repository, state: FSMContext ):
    await state.set_state(FighterCardStates.name)
    answer = 'Введите имя и фамилию бойца'
    await message.answer(answer)
@router.message(FighterCardStates.name)
async def get_card(message: Message,repository: Repository, state: FSMContext ):
    fighter = await repository.fighter.get_by_name(message.text)
    if fighter is None:
       await message.answer('Боец не найден')
    text = get_fighter_card(fighter)
    await message.answer(text)
    await state.clear()
def get_fighter_card(fighter: DBFighter):
    text = (f'Имя бойца - {fighter.name},\nвозраст - {fighter.age},\nстрана - {fighter.country},\nбазовый стиль - {fighter.base_style}, '
            f'\nгород - {fighter.city},\nрост - {fighter.height} см,\nвес - {fighter.weight} кг,\nвесовая категория - {fighter.weight_category},\nпродвижение - {fighter.promotion},\nразмах рук - {fighter.arm_span} см,'
            f'\nколичество побед - {fighter.wins_count},\nколичество поражений - {fighter.defeats_count},\nпобед нокаутом - {fighter.wins_knockouts_count},\nпоражений нокаутом - {fighter.defeats_knockouts_count}'
            f'\nпобед судейским решением - {fighter.wins_judges_decisions_count},\nпоражений судейским решением - {fighter.defeats_judges_decisions_count},\nсабмишн побед - {fighter.wins_submissions_count},\nсабмишн поражений - {fighter.defeats_submissions_count}')

    return text
