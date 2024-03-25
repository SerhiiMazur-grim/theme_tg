from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.types import InlineKeyboardMarkup


def choose_lang_ikb() -> InlineKeyboardMarkup:
    ikb = InlineKeyboardBuilder()
    
    ikb.button(text='Українська', callback_data='language_uk')
    ikb.button(text='Русский', callback_data='language_ru')
    ikb.button(text='English', callback_data='language_en')
    ikb.adjust(1)
    
    return ikb.as_markup()
