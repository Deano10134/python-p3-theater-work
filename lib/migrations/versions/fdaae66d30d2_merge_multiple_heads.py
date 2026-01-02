"""merge multiple heads

Revision ID: fdaae66d30d2
Revises: 001, 5baf64031b79
Create Date: 2026-01-02 16:09:25.259554

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'fdaae66d30d2'
down_revision = ('001', '5baf64031b79')
branch_labels = None
depends_on = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
