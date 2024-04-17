from aiogram.filters.callback_data import CallbackData


class FighterCallbackData(CallbackData, prefix='fighter'):
    fighter_id: int
class ForecastCallbackData(CallbackData, prefix='forecast'):
    first_fighter_id: int
    second_fighter_id: int