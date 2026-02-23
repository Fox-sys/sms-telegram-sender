from pydantic import BaseModel

from src.domain.sms_sender import SmsMessageDto
from src.presentation.api.v1.sms.schemes.sms_message import SmsMessageSchema


class SmsMessageBodySchema(BaseModel):
    messages: list[SmsMessageSchema]

    def to_domain(self) -> list[SmsMessageDto]:
        return [message.to_domain() for message in self.messages]
