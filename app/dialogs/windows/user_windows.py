from . import Window

from app.keyboards.inline_kb.user_ikb import (
    choose_device_ikb,
    choose_color_ikb,
    choose_alfa_ikb
)


CREATE_THEME_WINDOWS = {
    1: Window(
        message_key = 'messages-theme_create_choose_device',
        key_board = choose_device_ikb
    ),
    2: Window(
        message_key = 'messages-theme_create_choose_color_1',
        key_board = choose_color_ikb
    ),
    3: Window(
        message_key = 'messages-theme_create_choose_color_2',
        key_board = choose_color_ikb
    ),
    4: Window(
        message_key = 'messages-theme_create_choose_color_3',
        key_board = choose_color_ikb
    ),
    5: Window(
        message_key = 'messages-theme_create_choose_alfa',
        key_board=choose_alfa_ikb
    ),
}
