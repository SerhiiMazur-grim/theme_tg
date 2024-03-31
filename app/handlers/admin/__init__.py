from typing import Final

from aiogram import Router

from . import commands_handler

router: Final[Router] = Router(name=__name__)
router.include_routers(commands_handler.router)
