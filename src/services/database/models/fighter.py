from datetime import datetime
from typing import TYPE_CHECKING

from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base import Base, TimestampMixin, Int64, Int16

if TYPE_CHECKING:
    from .fight import DBFight


class DBFighter(Base, TimestampMixin):
    __tablename__ = "fighters"

    id: Mapped[Int64] = mapped_column(primary_key=True)
    name: Mapped[str]
    country: Mapped[str]
    base_style: Mapped[str]
    promotion: Mapped[str]
    city: Mapped[str]
    age: Mapped[Int16]
    date_of_birth: Mapped[datetime]
    weight: Mapped[Int16]
    height: Mapped[Int16]
    weight_category: Mapped[str]
    arm_span: Mapped[Int16]
    wins_count: Mapped[Int16]
    wins_knockouts_count: Mapped[Int16]
    wins_submissions_count: Mapped[Int16]
    wins_judges_decisions_count: Mapped[Int16]
    defeats_count: Mapped[Int16]
    defeats_knockouts_count: Mapped[Int16]
    defeats_submissions_count: Mapped[Int16]
    defeats_judges_decisions_count: Mapped[Int16]

