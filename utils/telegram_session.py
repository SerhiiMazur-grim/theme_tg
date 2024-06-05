import asyncio

from config import SESSIONS_NAME


free_sessions = SESSIONS_NAME.copy()


class SessionPool():
    
    async def _get_session(self) -> str:
        pending = True
        while pending:
            if free_sessions:
                session_name: str = free_sessions.pop()
                pending = False
            else:
                await asyncio.sleep(1)
        return session_name
    
    
    async def _return_session_to_pool(self, session_name: str) -> None:
        free_sessions.append(session_name)
