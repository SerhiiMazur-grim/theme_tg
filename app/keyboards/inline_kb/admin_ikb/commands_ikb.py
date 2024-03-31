from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.types import InlineKeyboardMarkup
from aiogram_i18n import I18nContext


def abort_get_image_for_id_ikb(i18n: I18nContext, language: str) -> InlineKeyboardMarkup:
    ikb = InlineKeyboardBuilder()
    
    ikb.button(text=i18n.core.get('ik_button-abort', language), callback_data='abort_get_image_for_id')
    ikb.adjust(1)
    
    return ikb.as_markup()
