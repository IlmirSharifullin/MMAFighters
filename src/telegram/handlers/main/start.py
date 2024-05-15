from aiogram import Router, Bot
from aiogram.filters import CommandStart
from aiogram.fsm.context import FSMContext
from aiogram.types import Message
from src.telegram.keyboards.menu import select_data

router = Router(name='start-command')


@router.message(CommandStart())
async def get_inline(message: Message, state: FSMContext):
    await state.clear()
    await message.answer(
        f'{message.from_user.first_name}, рад тебя видеть. Меня зовут MMAFighters bot. Я могу рассказать про бои и бойцов из мира MMA. Также я могу дать прогноз на следующий бой',
        reply_markup=select_data)
