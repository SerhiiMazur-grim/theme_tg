from aiogram import Bot
from aiogram.types import BotCommand, BotCommandScopeAllPrivateChats


async def set_commands(bot: Bot) -> None:
    all_private_chats_commands = [
        BotCommand(command='start',
                   description='–  Start dialog with bot'),
        BotCommand(command='language',
                   description='–  Change the language'),
    ]
    await bot.set_my_commands(commands=all_private_chats_commands,
                              scope=BotCommandScopeAllPrivateChats())
