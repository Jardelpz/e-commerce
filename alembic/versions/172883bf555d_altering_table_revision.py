"""altering table revision

Revision ID: 172883bf555d
Revises: a64500cc6c70
Create Date: 2021-01-31 14:11:00.224226

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '172883bf555d'
down_revision = 'a64500cc6c70'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column("users", sa.Column("job", sa.String()))
    pass


def downgrade():
    pass
