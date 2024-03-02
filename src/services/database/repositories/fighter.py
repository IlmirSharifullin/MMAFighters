import datetime
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

    async def insert(self, name: str, country: str, base_style: str, promotion: str, city: str, age: int,
                     date_of_birth: datetime.datetime, weight: int, height: int, weight_category: str, arm_span: int,
                     wins_count: int, wins_knockouts_count: int, wins_submissions_count: int,
                     wins_judges_decisions_count: int, defeats_count: int, defeats_knockouts_count: int,
                     defeats_submissions_count: int, defeats_judges_decisions_count: int) -> DBFighter:
        db_fighter: DBFighter = DBFighter(
            name=name,
            country=country,
            base_style=base_style,
            promotion=promotion,
            city=city,
            age=age,
            date_of_birth=date_of_birth,
            weight=weight,
            height=height,
            weight_category=weight_category,
            arm_span=arm_span,
            wins_count=wins_count,
            wins_knockouts_count=wins_knockouts_count,
            wins_submissions_count=wins_submissions_count,
            wins_judges_decisions_count=wins_judges_decisions_count,
            defeats_count=defeats_count,
            defeats_knockouts_count=defeats_knockouts_count,
            defeats_submissions_count=defeats_submissions_count,
            defeats_judges_decisions_count=defeats_judges_decisions_count
        )

        await self.commit(db_fighter)
        return db_fighter
