from aiogram.fsm.state import State, StatesGroup


class CreateThemeState(StatesGroup):
    step = State()
    end_step = State()
    color_list = State()
    wallpaper_path = State()
    device = State()
    bg_color = State()
    primary_color = State()
    secondary_color = State()
    alfa_chanel = State()
