"""add chat_id column to user

Revision ID: 26f751973a7d
Revises: fcd6f27b5708
Create Date: 2024-04-13 15:38:33.403479

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '26f751973a7d'
down_revision: Union[str, None] = 'fcd6f27b5708'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('chat_id', sa.Integer(), nullable=False))
    op.add_column('users', sa.Column('first_name', sa.String(), nullable=False))
    op.drop_column('users', 'name')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('name', sa.VARCHAR(), autoincrement=False, nullable=False))
    op.drop_column('users', 'first_name')
    op.drop_column('users', 'chat_id')
    # ### end Alembic commands ###
