from aiogram.utils.keyboard import ReplyKeyboardBuilder
from aiogram.types.reply_keyboard_markup import ReplyKeyboardMarkup
from aiogram_i18n import I18nContext


def main_keyboard(i18n: I18nContext, language: str | None = None) -> ReplyKeyboardMarkup:
    kb = ReplyKeyboardBuilder()
    if language:
        kb.button(text=i18n.core.get('button-create_theme', language))
        # kb.button(text=i18n.core.get('button-add_to_chat', language))
        # kb.button(text=i18n.core.get('button-catalog', language))
        # kb.button(text=i18n.core.get('button-faq', language))
    else:
        kb.button(text=i18n.button.create_theme())
        # kb.button(text=i18n.button.add_to_chat())
        # kb.button(text=i18n.button.catalog())
        # kb.button(text=i18n.button.faq())
    
    kb.adjust(1)
    return kb.as_markup(resize_keyboard=True)
    