"""Add posts table

Revision ID: 5470e4cbf1df
Revises: 39a5e2763edf
Create Date: 2023-12-24 21:28:04.640178

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '5470e4cbf1df'
down_revision: Union[str, None] = '39a5e2763edf'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    op.create_table('posts', sa.Column('id', sa.Integer(), nullable=False,
                    primary_key=True), sa.Column('title', sa.String(), nullable=False))
    pass


def downgrade():
    op.drop_table('posts')
    pass