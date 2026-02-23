from typing import Annotated, AsyncIterator

from fastapi import Depends, HTTPException
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from sqlalchemy.ext.asyncio import AsyncSession

from src.application.sms_sender.services import SmsSenderService
from src.infrastructure.database import (
    create_engine_from_settings,
    create_session_factory,
    DBSettings,
)
from src.infrastructure.database.repositories import SmsRepositoryImpl
from src.infrastructure.telegram.sender import TelegramSenderImpl
from src.infrastructure.telegram.settings import TelegramSettings
from src.presentation.api.settings import ApiSettings


class DB:
    settings = DBSettings()
    engine = create_engine_from_settings(settings=settings)
    session_factory = create_session_factory(engine=engine)


class ApiSecurity:
    api_settings = ApiSettings()


async def get_db_session_dependency() -> AsyncIterator[AsyncSession]:
    async with DB.session_factory() as session:
        try:
            yield session
            await session.commit()
        except Exception:
            await session.rollback()
            raise


def create_sms_repository(
    session: Annotated[AsyncSession, Depends(get_db_session_dependency)],
) -> SmsRepositoryImpl:
    return SmsRepositoryImpl(session=session)


def create_telegram_sender() -> TelegramSenderImpl:
    settings = TelegramSettings()
    url = f"https://api.telegram.org/bot{settings.BOT_TOKEN}/sendMessage"
    return TelegramSenderImpl(
        token=settings.BOT_TOKEN,
        chat_id=settings.CHAT_ID,
        url=url,
    )


def create_sms_sender_service(
    sms_repository: Annotated[SmsRepositoryImpl, Depends(create_sms_repository)],
    telegram_sender: Annotated[TelegramSenderImpl, Depends(create_telegram_sender)],
) -> SmsSenderService:
    return SmsSenderService(
        telegram_sender=telegram_sender,
        sms_repository=sms_repository,
    )


http_bearer = HTTPBearer()


async def require_bearer(
    credentials: Annotated[HTTPAuthorizationCredentials, Depends(http_bearer)],
) -> None:
    if credentials.credentials != ApiSecurity.api_settings.BEARER_TOKEN:
        raise HTTPException(status_code=401, detail="Invalid token")
