from pyrogram import Client
from pyrogram.raw.functions.account import UploadWallPaper
from pyrogram.raw.types import WallPaperSettings, WallPaper

from config.settings import Settings
from utils import SessionPool


SETTINGS: Settings = Settings()


class CreateWallpaper(SessionPool):
    api_id: int | str = SETTINGS.api_id.get_secret_value()
    api_hash: str = SETTINGS.api_hash.get_secret_value()
    
    
    async def get_wallpaper(self, wallpaper_path) -> WallPaper:
        session_name = await self._get_session()
        
        async with Client(session_name, self.api_id, self.api_hash) as app:
            file = await app.save_file(path=wallpaper_path)
            wallp: WallPaper = await app.invoke(UploadWallPaper(
                file=file,
                mime_type='image/jpeg',
                settings=WallPaperSettings()
            ))
            
        await self._return_session_to_pool(session_name)
        
        return wallp
