from aiogram.fsm.state import StatesGroup, State


class FighterCardStates(StatesGroup):
    name = State()