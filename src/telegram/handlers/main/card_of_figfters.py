from aiogram import Router, Bot, F
from aiogram.types import CallbackQuery
router = Router(name='card_of_fighters')
@router.callback_query(F.data=='card_of_fighters')
async def select_data(call: CallbackQuery, bot: Bot):
    answer = 'Прости, я пока не обладаю такой информацией'
    await call.message.answer(answer)
    await call.answer()