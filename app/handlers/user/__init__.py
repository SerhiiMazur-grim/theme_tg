from typing import Final

from aiogram import Router

from . import create_theme

router: Final[Router] = Router(name=__name__)
router.include_routers(create_theme.router)