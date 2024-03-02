from __future__ import annotations

from datetime import datetime

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from .base import Base, Int64, TimestampMixin


class DBFight(Base, TimestampMixin):
    __tablename__ = "fights"

    id: Mapped[Int64] = mapped_column(primary_key=True)
    first_fighter_id: Mapped[int] = mapped_column(ForeignKey("fighter.id"))
    second_fighter_id: Mapped[int] = mapped_column(ForeignKey("fighter.id"))
    date: Mapped[datetime]
    place: Mapped[str]

