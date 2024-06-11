from __future__ import annotations

from typing import TYPE_CHECKING, Any, Final

from aiogram import Router, F
from aiogram.filters import Command
from aiogram.methods import TelegramMethod
from aiogram.types import Message, CallbackQuery
from aiogram.fsm.context import FSMContext
from aiogram_i18n import I18nContext

from app.state.admin_state import AddThemeCategoryState
from app.keyboards.inline_kb.admin_ikb import abort_command_ikb

if TYPE_CHECKING:
    from services.database import Repository, ThemeCategory


router: Final[Router] = Router(name=__name__)


@router.message(Command('add_theme_category'))
async def add_theme_category_command(message: Message, i18n: I18nContext,
                               state: FSMContext) -> TelegramMethod[Any]:
    await message.delete()
    await state.set_state(AddThemeCategoryState.categories)
    return message.answer(text=i18n.messages.provide_category(),
                          reply_markup=abort_command_ikb(i18n))


@router.message(AddThemeCategoryState.categories)
async def get_categories(message: Message, i18n: I18nContext, 
                         state: FSMContext, repository: Repository) -> TelegramMethod[Any]:
    if message.text:
        categories = message.text.split('\n')
        if not len(categories) == 3:
            return message.answer(text=i18n.messages.not_all_localization_options())
        await state.clear()
        await repository.theme_category.create(*categories)
        
        return message.answer(text=i18n.messages.category_add_to_db())
    else:
        return message.answer(text=i18n.messages.is_not_localization_options())

