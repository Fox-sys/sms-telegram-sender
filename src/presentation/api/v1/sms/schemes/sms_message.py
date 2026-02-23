from pydantic import BaseModel

from src.domain.sms_sender import SmsMessageDto


class SmsMessageSchema(BaseModel):
    index: int
    phone: str
    content: str
    date: str
    smstat: int
    sms_type: int

    def to_domain(self) -> SmsMessageDto:
        return SmsMessageDto(
            index=self.index,
            phone=self.phone,
            content=self.content,
            date=self.date,
            smstat=self.smstat,
            sms_type=self.sms_type,
        )
