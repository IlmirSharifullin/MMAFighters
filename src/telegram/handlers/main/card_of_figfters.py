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
    text = (f'Имя бойца - {fighter.name}, возраст - {fighter.age}, страна - {fighter.country}, базовый стиль - {fighter.base_style}, '
            f' город - {fighter.city}, рост - {fighter.height} см, вес - {fighter.weight} кг, весовая категория - {fighter.weight_category}, продвижение - {fighter.promotion}, размах рук - {fighter.arm_span} см,'
            f' количество побед - {fighter.wins_count}, количество поражений - {fighter.defeats_count}, побед нокаутом - {fighter.wins_knockouts_count}, поражений нокаутом - {fighter.defeats_knockouts_count}'
            f'побед судейским решением - {fighter.wins_judges_decisions_count}, поражений судейским решением - {fighter.defeats_judges_decisions_count}, сабмишн побед - {fighter.wins_submissions_count}, сабмишн поражений - {fighter.defeats_submissions_count}')

    return text
