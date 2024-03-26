from aiogram.filters.callback_data import CallbackData


class FighterCallbackData(CallbackData, prefix='fighter'):
    fighter_id: int