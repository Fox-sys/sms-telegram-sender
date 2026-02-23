from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class SmsMessageDto:
    index: int
    phone: str
    content: str
    date: str
    smstat: int
    sms_type: int
