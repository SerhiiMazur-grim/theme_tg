import os

from aiogram import Bot


async def download_photo_from_user(user_id: str | int, photo_id: str, bot: Bot) -> str:
    user_id = str(user_id)
    prepare_downloading = await bot.get_file(photo_id)
    file_name = prepare_downloading.file_path.split('/')[-1]
    user_folder = os.path.join('src', 'users_data', user_id)
    
    if not os.path.exists(user_folder):
        os.makedirs(user_folder)
    
    download_to = os.path.join('src', 'users_data', user_id, file_name)
    await bot.download_file(file_path=prepare_downloading.file_path,
                            destination=download_to)
    return download_to
