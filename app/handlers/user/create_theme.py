from __future__ import annotations

from typing import Any, Final

from aiogram import Router, F, Bot
from aiogram.methods import TelegramMethod
from aiogram.types import Message, CallbackQuery, FSInputFile
from aiogram.fsm.context import FSMContext

from aiogram_i18n import I18nContext, LazyProxy

from app.keyboards.reply_kb.user_rkb import back_to_main_keyboard
from app.state.user_state import CreateThemeState
from app.dialogs.user_dialogs import CreateThemeDialog
from app.dialogs.windows import CREATE_THEME_WINDOWS as windows
from app.filters import PrivateChatFilter
from utils.theme import is_photo_id, wallp_answer_data


router: Final[Router] = Router(name=__name__)


@router.message(PrivateChatFilter(), F.text == LazyProxy('button-create_theme'))
async def create_theme_message(message: Message, i18n: I18nContext, state: FSMContext) -> TelegramMethod:
    await state.set_state(CreateThemeState.wallpaper_id)
    return message.answer(text=i18n.messages.create_theme_message(),
                          reply_markup=back_to_main_keyboard(i18n))


@router.message(CreateThemeState.wallpaper_id)
async def get_wallpaper(message: Message, bot: Bot, i18n: I18nContext, state: FSMContext):
    photo_id = is_photo_id(message)
    if not photo_id:
        return message.reply(i18n.messages.is_not_image_for_get_id())
    
    wait_message = await message.answer(text=i18n.messages.image_processing())
    step, image_path = await wallp_answer_data(message, photo_id, bot, state)
    
    window = windows.get(step)
    await wait_message.delete()
    
    return message.answer_photo(
        photo=FSInputFile(path=image_path),
        caption=window.caption(i18n),
        reply_markup=window.key_board(i18n)
    )


@router.callback_query(CreateThemeState.step)
async def theme_dialog(call: CallbackQuery, bot: Bot, state: FSMContext, i18n: I18nContext):
    dialog = CreateThemeDialog(call, bot, state, i18n)
    return await dialog.step_processing()
