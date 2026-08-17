"""add filename to templates

Revision ID: 682ca5e7c8ea
Revises: 4a58892bc51d
Create Date: 2026-08-13 13:32:00.584670

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "682ca5e7c8ea"
down_revision: Union[str, Sequence[str], None] = "4a58892bc51d"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""

    # ---------------------------------------------------------
    # 1. Add filename temporarily as nullable
    # ---------------------------------------------------------

    op.add_column(
        "templates",
        sa.Column(
            "filename",
            sa.String(length=500),
            nullable=True,
        ),
    )

    # ---------------------------------------------------------
    # 2. Set filenames for existing templates
    # ---------------------------------------------------------

    op.execute(
        """
        UPDATE templates
        SET filename = 'template1/index.html'
        WHERE id = 'tpl_Og1bMn'
        """
    )

    op.execute(
        """
        UPDATE templates
        SET filename = 'template2/index.html'
        WHERE id = 'tpl_eo5SOx'
        """
    )

    op.execute(
        """
        UPDATE templates
        SET filename = 'template3/index.html'
        WHERE id = 'tpl_cGiA1S'
        """
    )

    op.execute(
        """
        UPDATE templates
        SET filename = 'template4/index.html'
        WHERE id = 'tpl_cF2Q0X'
        """
    )

    # ---------------------------------------------------------
    # 3. Make filename required
    # ---------------------------------------------------------

    op.alter_column(
        "templates",
        "filename",
        existing_type=sa.String(length=500),
        nullable=False,
    )


def downgrade() -> None:
    """Downgrade schema."""

    op.drop_column(
        "templates",
        "filename",
    )