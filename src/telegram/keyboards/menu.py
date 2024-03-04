from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

select_data = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(
            text='Следующий бой',
            callback_data='next_fight'
        )
    ],
    [
        InlineKeyboardButton(
            text='Предыдущий бой',
            callback_data='past_fight'
        )
    ],
    [
        InlineKeyboardButton(
            text='Поиск по имени и фамилии бойца',
            callback_data='search_fighters'
        )
    ],
    [
        InlineKeyboardButton(
            text='Карточка статистики бойца',
            callback_data='card_of_fighters'
        )
    ]
])