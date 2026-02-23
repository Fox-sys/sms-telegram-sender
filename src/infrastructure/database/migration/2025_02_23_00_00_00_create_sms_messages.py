from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa

revision: str = "20250223000000"
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "sms_messages",
        sa.Column("id", sa.Integer(), autoincrement=True, nullable=False),
        sa.Column("index", sa.Integer(), nullable=False),
        sa.Column("phone", sa.String(length=32), nullable=False),
        sa.Column("content", sa.Text(), nullable=False),
        sa.Column("date", sa.String(length=64), nullable=False),
        sa.Column("smstat", sa.Integer(), nullable=False),
        sa.Column("sms_type", sa.Integer(), nullable=False),
        sa.Column(
            "created_at",
            sa.DateTime(),
            server_default=sa.text("(CURRENT_TIMESTAMP)"),
            nullable=False,
        ),
        sa.PrimaryKeyConstraint("id", name=op.f("pk_sms_messages")),
    )


def downgrade() -> None:
    op.drop_table("sms_messages")
