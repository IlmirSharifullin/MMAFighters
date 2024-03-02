from __future__ import annotations

from datetime import datetime
from typing import TYPE_CHECKING

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base import Base, Int64, TimestampMixin

if TYPE_CHECKING:
    from .fighter import DBFighter


class DBFight(Base, TimestampMixin):
    __tablename__ = "fights"

    id: Mapped[Int64] = mapped_column(primary_key=True)
    first_fighter_id: Mapped[int] = mapped_column(ForeignKey("fighter.id"))
    second_fighter_id: Mapped[int] = mapped_column(ForeignKey("fighter.id"))
    date: Mapped[datetime]
    place: Mapped[str]

    first_fighter: Mapped["DBFighter"] = relationship(foreign_keys=[first_fighter_id])
    second_fighter: Mapped["DBFighter"] = relationship(foreign_keys=[second_fighter_id])

