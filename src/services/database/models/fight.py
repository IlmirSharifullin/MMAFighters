from __future__ import annotations

from sqlalchemy.orm import Mapped, mapped_column

from .base import Base, Int64, TimestampMixin


class DBFight(Base, TimestampMixin):
    __tablename__ = "fights"

    id: Mapped[Int64] = mapped_column(primary_key=True)
    first_fighter: ...
    second_fighter: ...
