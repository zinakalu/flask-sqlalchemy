"""empty message

Revision ID: 824ed6ab57be
Revises: 6ddf97a54a17
Create Date: 2023-07-02 07:27:06.647465

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '824ed6ab57be'
down_revision = '6ddf97a54a17'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('pets', schema=None) as batch_op:
        batch_op.add_column(sa.Column('name', sa.String(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('pets', schema=None) as batch_op:
        batch_op.drop_column('name')

    # ### end Alembic commands ###
