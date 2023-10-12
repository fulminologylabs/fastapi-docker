"""base tables

Revision ID: 0f016313ed20
Revises: 
Create Date: 2023-10-11 21:27:12.850664

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '0f016313ed20'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('email', sa.String(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('created_at', sa.DateTime(), server_default=sa.text('statement_timestamp()'), nullable=False),
    sa.Column('updated_at', sa.DateTime(), nullable=True, onupdate=sa.text('statement_timestamp()')),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
    )
    op.create_index(op.f('ix_users_created_at'), 'users', ['created_at'], unique=False)
    op.create_index(op.f('ix_users_name'), 'users', ['name'], unique=True)
    op.create_index(op.f('ix_users_updated_at'), 'users', ['updated_at'], unique=False)
    
    op.create_table('item',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('title', sa.String(), nullable=False),
    sa.Column('description', sa.String(), nullable=False),
    sa.Column('created_at', sa.DateTime(), server_default=sa.text('statement_timestamp()'), nullable=False),
    sa.Column('updated_at', sa.DateTime(), nullable=True, onupdate=sa.text('statement_timestamp()')),
    sa.Column('owner_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['owner_id'], ['users.id'], onupdate='CASCADE', ondelete='RESTRICT'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_item_created_at'), 'item', ['created_at'], unique=False)
    op.create_index(op.f('ix_item_owner_id'), 'item', ['owner_id'], unique=False)
    op.create_index(op.f('ix_item_updated_at'), 'item', ['updated_at'], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_item_updated_at'), table_name='item')
    op.drop_index(op.f('ix_item_owner_id'), table_name='item')
    op.drop_index(op.f('ix_item_created_at'), table_name='item')
    op.drop_table('item')
    op.drop_index(op.f('ix_users_updated_at'), table_name='users')
    op.drop_index(op.f('ix_users_name'), table_name='users')
    op.drop_index(op.f('ix_users_created_at'), table_name='users')
    op.drop_table('users')
    # ### end Alembic commands ###
