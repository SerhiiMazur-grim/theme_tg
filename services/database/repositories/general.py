from __future__ import annotations

from sqlalchemy.ext.asyncio import AsyncSession

from .base import BaseRepository
from .user import UserRepository
from .theme_category import ThemeCategoryRepository


class Repository(BaseRepository):
    """
    The general repository.
    """

    user: UserRepository
    theme_category: ThemeCategoryRepository

    def __init__(self, session: AsyncSession) -> None:
        super().__init__(session=session)
        self.user = UserRepository(session=session)
        self.theme_category = ThemeCategoryRepository(session=session)
