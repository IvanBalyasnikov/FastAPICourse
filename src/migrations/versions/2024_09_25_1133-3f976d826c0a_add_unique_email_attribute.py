"""add unique email attribute

Revision ID: 3f976d826c0a
Revises: 78be158acaf4
Create Date: 2024-09-25 11:33:24.646618

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "3f976d826c0a"
down_revision: Union[str, None] = "78be158acaf4"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_unique_constraint(None, "users", ["email"])


def downgrade() -> None:
    op.drop_constraint(None, "users", type_="unique")
