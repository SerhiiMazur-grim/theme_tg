from __future__ import annotations

from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from .base import Base, Int64, TimestampMixin


class ThemeCategory(Base, TimestampMixin):
    __tablename__ = "theme_categories"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    
    ua_local: Mapped[str] = mapped_column(String(length=20))
    ru_local: Mapped[str] = mapped_column(String(length=20))
    en_local: Mapped[str] = mapped_column(String(length=20))
