from __future__ import annotations

from typing import Any, Final

from aiogram import Router, F
from aiogram.methods import TelegramMethod
from aiogram.types import Message

from aiogram_i18n import I18nContext, LazyProxy

router: Final[Router] = Router(name=__name__)


@router.message(F.text == LazyProxy('button-create_theme'))
async def create_theme_message(message: Message, i18n: I18nContext) -> TelegramMethod:
    return message.answer(text=i18n.messages.create_theme_message())
