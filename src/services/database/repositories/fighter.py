from typing import Optional, cast

from sqlalchemy import select

from ..models import DBFighter
from .base import BaseRepository


class FighterRepository(BaseRepository):
    async def get(self, fighter_id: int) -> Optional[DBFighter]:
        return cast(
            Optional[DBFighter],
            await self._session.scalar(select(DBFighter).where(DBFighter.id == fighter_id)),
        )
