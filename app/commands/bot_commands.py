from aiogram import Bot
from aiogram.types import BotCommand, BotCommandScopeAllPrivateChats, BotCommandScopeChat

from config.settings import Settings


async def set_commands(bot: Bot, settings: Settings) -> None:
    admin_id: int = settings.admin_chat_id
    
    all_private_chats_commands = [
        BotCommand(command='start',
                   description='–  Start dialog with bot'),
        BotCommand(command='language',
                   description='–  Change the language'),
    ]
    admin_commands = [
        BotCommand(command='image_id',
                   description='–  Get the image ID')
    ]
    admin_commands = all_private_chats_commands + admin_commands
    
    await bot.set_my_commands(commands=all_private_chats_commands,
                              scope=BotCommandScopeAllPrivateChats())
    await bot.set_my_commands(commands=admin_commands,
                              scope=BotCommandScopeChat(chat_id=admin_id))
