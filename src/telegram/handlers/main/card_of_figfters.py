from aiogram import Router, F
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from src.services.database import Repository, DBFighter
from src.telegram.handlers.main.get_fighter_card import get_fighter_card
from src.telegram.states import FighterCardStates

router = Router(name='card_of_fighters')


@router.message(F.text == 'Карточка бойца')
async def select_data(message: Message, repository: Repository, state: FSMContext):
    await state.set_state(FighterCardStates.name)
    answer = 'Введите имя и фамилию бойца'
    await message.answer(answer)


@router.message(FighterCardStates.name)
async def get_card(message: Message, repository: Repository, state: FSMContext):
    fighter = await repository.fighter.get_by_name(message.text)
    if fighter is None:
        await state.clear()
        return await message.answer('Боец не найден')

    text = get_fighter_card(fighter)
    await message.answer(text)
    await state.clear()
