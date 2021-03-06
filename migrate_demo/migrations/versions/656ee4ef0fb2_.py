"""empty message

Revision ID: 656ee4ef0fb2
Revises: 
Create Date: 2017-10-05 02:46:58.577581

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '656ee4ef0fb2'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('article',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=100), nullable=False),
    sa.Column('content', sa.Text(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('trade')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('trade',
    sa.Column('id', mysql.INTEGER(display_width=4, unsigned=True), nullable=False),
    sa.Column('name', mysql.VARCHAR(length=6), nullable=False),
    sa.Column('account', mysql.VARCHAR(length=11), nullable=False),
    sa.Column('saving', mysql.DECIMAL(unsigned=True, precision=8, scale=2), server_default=sa.text("'0.00'"), nullable=False),
    sa.Column('expend', mysql.DECIMAL(unsigned=True, precision=8, scale=2), server_default=sa.text("'0.00'"), nullable=False),
    sa.Column('income', mysql.DECIMAL(unsigned=True, precision=8, scale=2), server_default=sa.text("'0.00'"), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    mysql_default_charset='utf8',
    mysql_engine='InnoDB'
    )
    op.drop_table('article')
    # ### end Alembic commands ###
