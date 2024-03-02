import datetime
from typing import Optional, cast, TYPE_CHECKING

from sqlalchemy import select

from ..models import DBFight
from .base import BaseRepository

if TYPE_CHECKING:
    from ..models import DBFighter

    
class FightRepository(BaseRepository):
    async def get(self, fight_id: int) -> Optional[DBFight]:
        return cast(
            Optional[DBFight],
            await self._session.scalar(select(DBFight).where(DBFight.id == fight_id)),
        )

    async def insert(self, first_fighter: "DBFighter", second_fighter: "DBFighter", date: datetime.datetime, place: str):
        db_fight = DBFight(
            first_fighter=first_fighter,
            second_fighter=second_fighter,
            date=date,
            place=place
        )
        await self.commit(db_fight)
        return db_fight