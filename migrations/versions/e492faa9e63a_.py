# -*- coding: utf-8 -*-
"""empty message

Revision ID: e492faa9e63a
Revises: 3fc0b28658aa
Create Date: 2022-02-08 10:05:57.487115

"""
import sqlalchemy as sa
from alembic import op

import app
import app.extensions

# revision identifiers, used by Alembic.
revision = 'e492faa9e63a'
down_revision = '3fc0b28658aa'


def upgrade():
    """
    Upgrade Semantic Description:
        ENTER DESCRIPTION HERE
    """
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('sighting', schema=None) as batch_op:
        batch_op.add_column(sa.Column('id_configs', app.extensions.JSON(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    """
    Downgrade Semantic Description:
        ENTER DESCRIPTION HERE
    """
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('sighting', schema=None) as batch_op:
        batch_op.drop_column('id_configs')

    # ### end Alembic commands ###
