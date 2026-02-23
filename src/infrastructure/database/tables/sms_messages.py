import sqlalchemy as sa

from src.infrastructure.database.meta import metadata

sms_messages_table = sa.Table(
    "sms_messages",
    metadata,
    sa.Column("id", sa.Integer, primary_key=True, autoincrement=True),
    sa.Column("index", sa.Integer, nullable=False),
    sa.Column("phone", sa.String(32), nullable=False),
    sa.Column("content", sa.Text, nullable=False),
    sa.Column("date", sa.String(64), nullable=False),
    sa.Column("smstat", sa.Integer, nullable=False),
    sa.Column("sms_type", sa.Integer, nullable=False),
    sa.Column(
        "created_at",
        sa.DateTime,
        server_default=sa.func.now(),
        nullable=False,
    ),
)
