from __future__ import annotations

from typing import Any, Final

from aiogram import Router, F
from aiogram.methods import TelegramMethod
from aiogram.types import Message, CallbackQuery, InlineKeyboardMarkup
from aiogram.fsm.context import FSMContext

from aiogram_i18n import I18nContext, LazyProxy

from services.database import DBUser
from app.state.user_state import CreateThemeState
from app.dialogs.user_dialogs import CREATE_THEME_WINDOWS as windows, CreateThemeDialog


router: Final[Router] = Router(name=__name__)


@router.message(F.text == LazyProxy('button-create_theme'))
async def create_theme_message(message: Message, i18n: I18nContext) -> TelegramMethod:
    return message.answer(text=i18n.messages.create_theme_message())


@router.message(F.photo)
async def get_wallpaper(message: Message, i18n: I18nContext, state: FSMContext):
    await state.set_state(CreateThemeState.step)
    step = 0
    window = windows[step]
    wallpaper = message.photo[-1].file_id
    color_list = ['color1', 'color2']
    await state.set_data({
        'step': step,
        'wallpaper': wallpaper,
        'color_list': color_list
    })
    return message.answer_photo(
        photo='AgACAgIAAxkBAAICt2YJs1gsEJnI17Jx1v3ugyNOD14vAAL72jEbcEFJSI9TMYYd6nuiAQADAgADeQADNAQ',
        caption=window.caption(i18n),
        reply_markup=window.key_board(color_list)
    )


@router.callback_query(CreateThemeState.step)
async def theme_dialog(call: CallbackQuery, state: FSMContext, i18n: I18nContext):
    dialog = CreateThemeDialog(call, state, i18n)
    return await dialog.step_processing()
