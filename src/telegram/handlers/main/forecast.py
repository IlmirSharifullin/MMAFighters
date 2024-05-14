from aiogram import Router
from aiogram.types import CallbackQuery

from src.neuralnetwork.main import calculate_probability
from src.services.database import Repository
from src.telegram.callback_data import ForecastCallbackData

router = Router(name='forecast')
@router.callback_query(ForecastCallbackData.filter())
async def select_data(query: CallbackQuery,callback_data: ForecastCallbackData, repository: Repository ):
    fighter1 = await repository.fighter.get(callback_data.first_fighter_id)
    fighter2 = await repository.fighter.get(callback_data.second_fighter_id)
    probability_fighter1, probability_fighter2 = await calculate_probability(fighter1, fighter2)
    if probability_fighter1[0] > probability_fighter2[0]:
        text = (f'Победит {fighter1.name} (шанс на победу - {str(probability_fighter1[0] + 10)[:5]})')
    elif probability_fighter2[0] > probability_fighter1[0]:
        text = (f'Победит {fighter2.name} (шанс на победу - {str(probability_fighter2[0] + 10)[:5]})')
    else:
        text = (f'Шансы равны')
        text += (f'\n({fighter1.name} - {str(probability_fighter1[0])[:5]}')
        text += (f'\n{fighter2.name} - {str(probability_fighter2[0])[:5]})')

    await query.message.answer(text)
    await query.answer()