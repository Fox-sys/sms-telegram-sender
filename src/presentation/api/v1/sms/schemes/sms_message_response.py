from datetime import datetime

from pydantic import BaseModel

from src.domain.sms_sender import SmsMessageEntity


class SmsMessageResponseSchema(BaseModel):
    id: int
    index: int
    phone: str
    content: str
    date: str
    smstat: int
    sms_type: int
    created_at: datetime

    @classmethod
    def from_entity(cls, entity: SmsMessageEntity) -> "SmsMessageResponseSchema":
        return cls(
            id=entity.id or 0,
            index=entity.index,
            phone=entity.phone,
            content=entity.content,
            date=entity.date,
            smstat=entity.smstat,
            sms_type=entity.sms_type,
            created_at=entity.created_at or datetime.min,
        )
