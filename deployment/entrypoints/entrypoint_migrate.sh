#!/usr/bin/env bash
set -e
# Always use /data in container so the DB is created in the mounted volume
export DB_URL="sqlite+aiosqlite:////data/sms.db"
exec python -m src.run.alembic_runner upgrade head