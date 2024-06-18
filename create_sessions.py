import asyncio

from pyrogram import Client

from config import SESSIONS_NAME
from config.settings import Settings


SESSIONS: list = SESSIONS_NAME.copy()
SETTINGS = Settings()
API_ID: int | str = SETTINGS.api_id.get_secret_value()
API_HASH: str = SETTINGS.api_hash.get_secret_value()


async def create_session(sessions_names):
    for session in sessions_names:
        async with Client(session, API_ID, API_HASH) as app:
            try:
                me = await app.get_me()
                if me:
                    print(f'Session: {session} is created! \n')
                else:
                    print(f'WARNING !!! \n Session: {session} is not created! \n')
                    
            except Exception as e:
                print(f'ERROR {e} while create session: {session}\n')


async def main():
    await create_session(SESSIONS)


asyncio.run(main())
