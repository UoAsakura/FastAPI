"""Initial migration

Revision ID: cc6ef810b14e
Revises: 
Create Date: 2024-12-26 18:36:52.438864

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision: str = 'cc6ef810b14e'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('hotels',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('name', sa.String(), nullable=False),
                    sa.Column('location', sa.String(), nullable=False),
                    sa.Column('services', sa.JSON(), nullable=True),
                    sa.Column('rooms_quntity', sa.Integer(), nullable=False),
                    sa.Column('image_id', sa.Integer(), nullable=True),
                    sa.PrimaryKeyConstraint('id')
                    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('hotels')
    # ### end Alembic commands ###