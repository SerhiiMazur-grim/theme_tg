from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.types import InlineKeyboardMarkup


def choose_color_ikb(x) -> InlineKeyboardMarkup:
    ikb = InlineKeyboardBuilder()
    print(x)
    ikb.button(text='1', callback_data='#111111')
    ikb.button(text='2', callback_data='#222222')
    ikb.button(text='3', callback_data='#333333')
    ikb.button(text='4', callback_data='#444444')
    ikb.button(text='5', callback_data='#555555')
    ikb.button(text='White', callback_data='#ffffff')
    ikb.button(text='Black', callback_data='#000000')
    ikb.button(text='Auto', callback_data='auto')
    ikb.adjust(5,3)
    
    return ikb.as_markup()


def choose_alfa_ikb() -> InlineKeyboardMarkup:
    ikb = InlineKeyboardBuilder()
    
    ikb.button(text='10', callback_data='alfa_1')
    ikb.button(text='20', callback_data='alfa_2')
    ikb.button(text='30', callback_data='alfa_3')
    ikb.button(text='40', callback_data='alfa_4')
    ikb.button(text='50', callback_data='alfa_5')
    ikb.button(text='60', callback_data='alfa_6')
    ikb.button(text='70', callback_data='alfa_7')
    ikb.button(text='80', callback_data='alfa_8')
    ikb.button(text='90', callback_data='alfa_9')
    ikb.button(text='Без прозорості', callback_data='alfa_0')
    ikb.button(text='BACK', callback_data='previous_window')
    ikb.adjust(5,4,1,1)
    
    return ikb.as_markup()
