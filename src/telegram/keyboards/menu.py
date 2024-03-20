from aiogram.types import  ReplyKeyboardMarkup, KeyboardButton

select_data = ReplyKeyboardMarkup(keyboard=[
    [
        KeyboardButton(
            text='Следующий бой'
        )
    ],
    [
        KeyboardButton(
            text='Прогноз на следующий бой',
        )
    ,

        KeyboardButton(
            text='Карточка бойца',
        )
    ]
])