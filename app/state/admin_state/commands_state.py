from aiogram.fsm.state import State, StatesGroup


class GetImageIdState(StatesGroup):
    image = State()
