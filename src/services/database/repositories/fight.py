import datetime
from typing import Optional, cast, TYPE_CHECKING
import random

from sqlalchemy import select
from sqlalchemy.orm import joinedload

from ..models import DBFight
from .base import BaseRepository

if TYPE_CHECKING:
    from ..models import DBFighter


class FightRepository(BaseRepository):
    async def get(self, fight_id: int) -> Optional[DBFight]:
        return cast(
            Optional[DBFight],
            await self._session.scalar(select(DBFight).where(DBFight.id == fight_id).options(joinedload('*'))),
        )

    async def get_next(self):
        now = datetime.datetime.now()
        res = await self._session.execute(select(DBFight).where(DBFight.date > now).order_by(DBFight.date).options(joinedload('*')))
        res = res.fetchall()
        if res is not None and len(res) > 0:
            return res[0][0]
        else:
            return None

    async def get_random_n(self, n: int) -> list[DBFight]:
        res = await self._session.execute(select(DBFight).options(joinedload('*')))
        res = [x[0] for x in res.fetchall()]
        return random.choices(res, k=n)

    async def _exists(self, first_fighter_id: int, second_fighter_id: int, place: str, date: datetime.datetime):
        return cast(
            Optional[DBFight],
            await self._session.scalar(select(DBFight).where(DBFight.first_fighter_id == first_fighter_id,
                                                             DBFight.second_fighter_id == second_fighter_id,
                                                             DBFight.place == place,
                                                             DBFight.date == date).options(joinedload('*'))))

    async def create(self, first_fighter: "DBFighter", second_fighter: "DBFighter", date: datetime.datetime,
                     place: str) -> tuple[DBFight, bool]:
        """
        return: tuple[DBFight, bool(if dbfight already exists True, else False)]
        """
        existing_fight = await self._exists(first_fighter_id=first_fighter.id, second_fighter_id=second_fighter.id,
                                            place=place, date=date)

        if existing_fight is None:
            db_fight = DBFight(
                first_fighter=first_fighter,
                second_fighter=second_fighter,
                first_fighter_id=first_fighter.id,
                second_fighter_id=second_fighter.id,
                date=date,
                place=place
            )
            await self.commit(db_fight)
            return db_fight, True

        return existing_fight, False
