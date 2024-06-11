from typing import Optional, cast

from aiogram.enums import ChatType
from aiogram.types import Chat, User
from sqlalchemy import select, update, values, delete

from ..models import ThemeCategory
from .base import BaseRepository


class ThemeCategoryRepository(BaseRepository):
    
    async def get(self, category_id: int) -> Optional[ThemeCategory]:
        return cast(
            Optional[ThemeCategory],
            await self._session.scalar(select(ThemeCategory).where(ThemeCategory.id == category_id)),
        )
    
    
    async def get_all(self) -> Optional[ThemeCategory]:
        return cast(
            Optional[ThemeCategory],
            await self._session.scalars(select(ThemeCategory)),
        )


    async def create(self, ua_local: str, ru_local: str, en_local: str,) -> ThemeCategory:
        db_theme_category: ThemeCategory = ThemeCategory(
            ua_local = ua_local,
            ru_local = ru_local,
            en_local = en_local
        )

        await self.commit(db_theme_category)
        return db_theme_category
    
    
    async def delete(self, category_id: int) -> None:
        category: ThemeCategory = await self._session.scalar(
            delete(ThemeCategory)
            .where(ThemeCategory.id == category_id)
        )
        await self.commit(category)        
