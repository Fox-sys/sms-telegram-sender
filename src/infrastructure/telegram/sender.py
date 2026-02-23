import aiohttp
from attr import frozen

from src.application.sms_sender.interfaces.telegram_sender import TelegramSender


@frozen
class TelegramSenderImpl(TelegramSender):
    token: str
    chat_id: str
    url: str

    async def send_message(self, text: str) -> None:
        async with aiohttp.ClientSession() as session:
            await session.post(
                self.url,
                json={"chat_id": self.chat_id, "text": text},
            )
