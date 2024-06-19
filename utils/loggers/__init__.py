import logging

from config.settings import Settings
from .multiline import MultilineLogger

__all__ = ["database", "webhook", "setup_logger", "MultilineLogger"]

webhook: logging.Logger = logging.getLogger("bot.webhook")
database: logging.Logger = logging.getLogger("bot.database")


def setup_logger(level: int = logging.INFO) -> None:
    settings = Settings()
    logging_info = settings.logging_info
    
    if not logging_info:
        level = logging.WARNING
    
    for name in ["aiogram.middlewares", "aiogram.event", "aiohttp.access"]:
        logging.getLogger(name).setLevel(logging.WARNING)

    logging.basicConfig(
        format="%(asctime)s %(levelname)s | %(name)s: %(message)s",
        datefmt="[%H:%M:%S]",
        level=level,
    )
    # logging.basicConfig(
    #     filename='theme-bot.log',
    #     format="%(asctime)s %(levelname)s | %(name)s: %(message)s",
    #     datefmt="[%H:%M:%S]",
    #     level=level,
    # )
