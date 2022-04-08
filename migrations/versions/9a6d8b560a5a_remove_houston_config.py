# -*- coding: utf-8 -*-
"""remove houston_config

Revision ID: 9a6d8b560a5a
Revises: fd467d5e0812
Create Date: 2022-03-18 20:47:33.020537

"""
from alembic import op
import sqlalchemy as sa

import app.extensions


# revision identifiers, used by Alembic.
revision = '9a6d8b560a5a'
down_revision = 'fd467d5e0812'


def upgrade():
    """
    Upgrade Semantic Description:
        ENTER DESCRIPTION HERE
    """
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('houston_config', schema=None) as batch_op:
        batch_op.drop_index('ix_houston_config_created')
        batch_op.drop_index('ix_houston_config_indexed')
        batch_op.drop_index('ix_houston_config_updated')

    op.drop_table('houston_config')
    # ### end Alembic commands ###


def downgrade():
    """
    Downgrade Semantic Description:
        ENTER DESCRIPTION HERE
    """
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        'houston_config',
        sa.Column('created', sa.DateTime(), autoincrement=False, nullable=False),
        sa.Column('updated', sa.DateTime(), autoincrement=False, nullable=False),
        sa.Column('viewed', sa.DateTime(), autoincrement=False, nullable=False),
        sa.Column('guid', app.extensions.GUID(), autoincrement=False, nullable=False),
        sa.Column('key', sa.String(), autoincrement=False, nullable=False),
        sa.Column(
            'value',
            sa.JSON(),
            autoincrement=False,
            nullable=False,
        ),
        sa.Column(
            'indexed',
            sa.DateTime(),
            server_default=sa.text('CURRENT_TIMESTAMP'),
            autoincrement=False,
            nullable=False,
        ),
        sa.PrimaryKeyConstraint('guid', name=op.f('pk_houston_config')),
        sa.UniqueConstraint('key', name=op.f('uq_houston_config_key')),
    )
    with op.batch_alter_table('houston_config', schema=None) as batch_op:
        batch_op.create_index('ix_houston_config_updated', ['updated'], unique=False)
        batch_op.create_index('ix_houston_config_indexed', ['indexed'], unique=False)
        batch_op.create_index('ix_houston_config_created', ['created'], unique=False)

    # ### end Alembic commands ###
