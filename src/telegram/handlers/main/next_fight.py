from aiogram import Router, Bot, F
from aiogram.types import CallbackQuery
router = Router(name='next_fight')
@router.callback_query(F.data=='next_fight')
async def select_data(call: CallbackQuery, bot: Bot):
    answer = 'Прости, я пока не обладаю такой информацией'
    await call.message.answer(answer)
    await call.answer()