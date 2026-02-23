from typing import Protocol


class TelegramSender(Protocol):
    async def send_message(self, text: str) -> None: ...
