from collections.abc import AsyncGenerator

from sqlalchemy.ext.asyncio import AsyncSession

from src.infrastructure.database.engine import session_factory


async def get_session() -> AsyncGenerator[AsyncSession, None]:
    async with session_factory() as session:
        yield session
