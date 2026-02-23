from sqlalchemy.orm import registry

from src.domain.sms_sender import SmsMessageEntity
from src.infrastructure.database.tables import sms_messages_table

mapper = registry()
mapper.map_imperatively(SmsMessageEntity, sms_messages_table)
