from typing import Optional, cast

from sqlalchemy import select

from ..models import DBFight
from .base import BaseRepository


class FightRepository(BaseRepository):
    async def get(self, fight_id: int) -> Optional[DBFight]:
        return cast(
            Optional[DBFight],
            await self._session.scalar(select(DBFight).where(DBFight.id == fight_id)),
        )
