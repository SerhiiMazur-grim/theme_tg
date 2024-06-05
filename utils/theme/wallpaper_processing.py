from aiogram import Bot
from aiogram.types import Message
from aiogram.fsm.context import FSMContext

from . import (
    download_photo_from_user,
    get_colors,
    create_colorpic_image
)
from app.state.user_state import CreateThemeState


async def wallp_answer_data(message: Message, photo_id: str, bot: Bot, state: FSMContext):
    user_id = message.from_user.id
    download_photo: str = await download_photo_from_user(user_id, photo_id, bot)
    colors: list = await get_colors(download_photo)
    wallpaper_path: str = await create_colorpic_image(colors, user_id)
    
    await state.set_state(CreateThemeState.step)
    
    step = 1
    
    await state.update_data({
        'chat_id': user_id,
        'photo_message': message,
        'step': step,
        'wallpaper_id': photo_id,
        'color_list': colors,
        'wallpaper_path': download_photo
    })
    
    return step, wallpaper_path
