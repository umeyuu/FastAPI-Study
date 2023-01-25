"""create_first_tables

Revision ID: 784e7ce78254
Revises: 
Create Date: 2023-01-25 18:19:12.059667

"""

import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic
revision = '784e7ce78254'
down_revision = None
branch_labels = None
depends_on = None


def create_hedgehogs_table() -> None:
    op.create_table(
        "hedgehogs",
        sa.Column("id", sa.Integer, primary_key=True),
        sa.Column("name", sa.Text, nullable=False, index=True),
        sa.Column("description", sa.Text, nullable=True),
        sa.Column("color_type", sa.Text, nullable=False),
        sa.Column("age", sa.Numeric(10, 1), nullable=False),
    )


def upgrade() -> None:
    create_hedgehogs_table()


def downgrade() -> None:
    op.drop_table("hedgehogs")