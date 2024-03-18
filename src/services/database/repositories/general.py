from __future__ import annotations

from sqlalchemy.ext.asyncio import AsyncSession

from .base import BaseRepository
from .user import UserRepository
from .fighter import FighterRepository
from .fight import FightRepository


class Repository(BaseRepository):
    """
    The general repository.
    """

    user: UserRepository
    fighter: FighterRepository
    fight: FightRepository

    def __init__(self, session: AsyncSession) -> None:
        super().__init__(session=session)
        self.user = UserRepository(session=session)
        self.fighter = FighterRepository(session=session)
        self.fight = FightRepository(session=session)
