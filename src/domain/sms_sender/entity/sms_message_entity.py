from dataclasses import dataclass
from datetime import datetime


@dataclass
class SmsMessageEntity:
    index: int
    phone: str
    content: str
    date: str
    smstat: int
    sms_type: int
    id: int | None = None
    created_at: datetime | None = None
