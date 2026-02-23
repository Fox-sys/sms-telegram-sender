from sqlalchemy.ext.asyncio import AsyncEngine, create_async_engine, AsyncSession, async_sessionmaker

from src.infrastructure.database.settings import DBSettings


def create_engine_from_settings(settings: DBSettings) -> AsyncEngine:
    engine_kwargs: dict = {"echo": settings.DB_ECHO}
    if "sqlite" not in settings.DB_URL:
        engine_kwargs.update({
            "pool_size": 20,
            "max_overflow": 10,
            "pool_pre_ping": True,
        })
    return create_async_engine(settings.DB_URL, **engine_kwargs)


def create_session_factory(engine: AsyncEngine) -> async_sessionmaker[AsyncSession]:
    return async_sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)


_db_settings = DBSettings()
engine = create_engine_from_settings(_db_settings)
session_factory = create_session_factory(engine)
