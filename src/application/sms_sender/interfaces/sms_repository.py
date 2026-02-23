from typing import Protocol

from src.domain.sms_sender import SmsMessageDto, SmsMessageEntity


class SmsRepository(Protocol):
    async def bulk_create(self, messages: list[SmsMessageDto]) -> None: ...

    async def get_all(self) -> list[SmsMessageEntity]: ...
