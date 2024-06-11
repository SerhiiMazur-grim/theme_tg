from typing import Final

from aiogram import Router

from .commands_handlers import image_id, add_theme_category, abort_command


router: Final[Router] = Router(name=__name__)
router.include_routers(image_id.router, add_theme_category.router, abort_command.router)
