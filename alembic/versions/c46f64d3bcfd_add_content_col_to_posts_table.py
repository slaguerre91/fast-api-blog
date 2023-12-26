"""Add content col to posts table

Revision ID: c46f64d3bcfd
Revises: 5dbfbf0566d3
Create Date: 2023-12-24 21:29:43.957710

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'c46f64d3bcfd'
down_revision: Union[str, None] = '5dbfbf0566d3'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade():
    op.drop_column('posts', 'content')
    pass
