from attr import frozen

from src.domain.sms_sender import SmsMessageDto, SmsMessageEntity
from src.application.sms_sender.interfaces import SmsRepository, TelegramSender


@frozen
class SmsSenderService:
    telegram_sender: TelegramSender
    sms_repository: SmsRepository

    def _format_text(self, messages: list[SmsMessageDto]) -> str:
        lines = []
        for message in messages:
            lines.append(
                f"📱 [{message.index}] {message.phone}\n"
                f"📅 {message.date}\n"
                f"📝 {message.content}\n"
                f"stat={message.smstat} type={message.sms_type}"
            )
        return "\n\n---\n\n".join(lines)

    async def save_and_notify(self, messages: list[SmsMessageDto]) -> None:
        if not messages:
            return
        await self.sms_repository.bulk_create(messages)
        text = self._format_text(messages)
        await self.telegram_sender.send_message(text)

    async def get_all_messages(self) -> list[SmsMessageEntity]:
        return await self.sms_repository.get_all()
