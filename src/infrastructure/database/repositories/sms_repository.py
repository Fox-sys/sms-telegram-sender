from sqlalchemy import select

from src.application.sms_sender.interfaces.sms_repository import SmsRepository
from src.domain.sms_sender import SmsMessageDto, SmsMessageEntity
from src.infrastructure.database.repositories.base import AsyncBaseRepo
from src.infrastructure.database.tables import sms_messages_table


class SmsRepositoryImpl(AsyncBaseRepo, SmsRepository):
    async def get_all(self) -> list[SmsMessageEntity]:
        result = await self.session.execute(
            select(SmsMessageEntity).order_by(SmsMessageEntity.created_at.desc())
        )
        return list(result.scalars().all())

    async def bulk_create(self, messages: list[SmsMessageDto]) -> None:
        if not messages:
            return
        rows = [
            {
                "index": message.index,
                "phone": message.phone,
                "content": message.content,
                "date": message.date,
                "smstat": message.smstat,
                "sms_type": message.sms_type,
            }
            for message in messages
        ]
        await self.session.execute(sms_messages_table.insert(), rows)
