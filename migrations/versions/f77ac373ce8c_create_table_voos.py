"""Create table Voos

Revision ID: f77ac373ce8c
Revises: 
Create Date: 2025-03-01 18:50:00.481990

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f77ac373ce8c'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('voos',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('ano', sa.Integer(), nullable=True),
    sa.Column('mes', sa.Integer(), nullable=True),
    sa.Column('mercado', sa.String(length=50), nullable=True),
    sa.Column('rpk', sa.Float(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('voos')
    # ### end Alembic commands ###
