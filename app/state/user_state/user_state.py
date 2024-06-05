from aiogram.fsm.state import State, StatesGroup


class CreateThemeState(StatesGroup):
    chat_id = State()
    photo_message = State()
    step = State()
    color_list = State()
    wallpaper_id = State()
    wallpaper_path = State()
    device = State()
    bg_color = State()
    primary_color = State()
    secondary_color = State()
    alfa_chanel = State()
