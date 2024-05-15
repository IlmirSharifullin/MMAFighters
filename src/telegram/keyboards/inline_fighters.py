from aiogram.filters import callback_data
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from src.telegram.callback_data import FighterCallbackData, ForecastCallbackData


def get_fight_info_keyboards(first_fighter_id,second_fighter_id,first_fighter_name,second_fighter_name):
    kb = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text=f'{first_fighter_name}', callback_data=FighterCallbackData(fighter_id=first_fighter_id).pack()),
        InlineKeyboardButton(text=f'{second_fighter_name}', callback_data=FighterCallbackData(fighter_id=second_fighter_id).pack())],
        [InlineKeyboardButton(text='Прогноз на бой',callback_data=ForecastCallbackData(first_fighter_id=first_fighter_id, second_fighter_id=second_fighter_id).pack())]
    ])
    return kb