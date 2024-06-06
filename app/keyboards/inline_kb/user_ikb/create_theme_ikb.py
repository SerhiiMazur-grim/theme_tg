from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.types import InlineKeyboardMarkup
from aiogram_i18n import I18nContext

from config.callback_data import (
    CANCEL_CREATE_THEME,
    THEME_STEP_BACK,
    AUTO_CREATE_THEME
)
from utils import get_text


def choose_device_ikb(i18n: I18nContext) -> InlineKeyboardMarkup:
    pc_text: str = get_text(i18n, 'ik_button-pc')
    cancel: str = get_text(i18n, 'ik_button-abort')
    
    ikb = InlineKeyboardBuilder()
    ikb.button(text='Android', callback_data='android')
    ikb.button(text='iPhone', callback_data='iphone')
    ikb.button(text=pc_text, callback_data='computer')
    ikb.button(text=cancel, callback_data=CANCEL_CREATE_THEME)
    ikb.adjust(1)
    
    return ikb.as_markup()


def choose_color_ikb(colors: list, i18n: I18nContext) -> InlineKeyboardMarkup:
    back: str = get_text(i18n, 'ik_button-back')
    cancel: str = get_text(i18n, 'ik_button-abort')
    
    ikb = InlineKeyboardBuilder()
    ikb.button(text='1', callback_data=colors[0])
    ikb.button(text='2', callback_data=colors[1])
    ikb.button(text='3', callback_data=colors[2])
    ikb.button(text='4', callback_data=colors[3])
    ikb.button(text='5', callback_data=colors[4])
    ikb.button(text='White', callback_data='#ffffff')
    ikb.button(text='Black', callback_data='#000000')
    ikb.button(text='Auto', callback_data=AUTO_CREATE_THEME)
    ikb.button(text=back, callback_data=THEME_STEP_BACK)
    ikb.button(text=cancel, callback_data=CANCEL_CREATE_THEME)
    ikb.adjust(5, 3, 2)
    
    return ikb.as_markup()


def choose_alfa_ikb(i18n: I18nContext) -> InlineKeyboardMarkup:
    back: str = get_text(i18n, 'ik_button-back')
    cancel: str = get_text(i18n, 'ik_button-abort')
    no_alfa: str = get_text(i18n, 'ik_button-no_alfa')
    
    ikb = InlineKeyboardBuilder()
    ikb.button(text='10%', callback_data='e6')
    ikb.button(text='20%', callback_data='cc')
    ikb.button(text='30%', callback_data='b3')
    ikb.button(text='40%', callback_data='99')
    ikb.button(text='50%', callback_data='80')
    ikb.button(text='60%', callback_data='66')
    ikb.button(text='70%', callback_data='4d')
    ikb.button(text='80%', callback_data='33')
    ikb.button(text='90%', callback_data='1a')
    ikb.button(text=no_alfa, callback_data='ff')
    ikb.button(text=back, callback_data=THEME_STEP_BACK)
    ikb.button(text=cancel, callback_data=CANCEL_CREATE_THEME)
    ikb.adjust(5, 4, 1, 2)
    
    return ikb.as_markup()
