from fastapi import APIRouter, Depends

from src.application.sms_sender.services import SmsSenderService
from src.presentation.api.dependencies import create_sms_sender_service, require_bearer
from src.presentation.api.v1.sms.schemes.sms_message_body import SmsMessageBodySchema
from src.presentation.api.v1.sms.schemes.sms_message_response import SmsMessageResponseSchema

router = APIRouter()


@router.get("/messages", response_model=list[SmsMessageResponseSchema])
async def list_messages(
    service: SmsSenderService = Depends(create_sms_sender_service),
    _: None = Depends(require_bearer),
) -> list[SmsMessageResponseSchema]:
    entities = await service.get_all_messages()
    return [SmsMessageResponseSchema.from_entity(entity) for entity in entities]


@router.post("/send")
async def send_sms(
    body: SmsMessageBodySchema,
    service: SmsSenderService = Depends(create_sms_sender_service),
    _: None = Depends(require_bearer),
) -> dict[str, str]:
    await service.save_and_notify(body.to_domain())
    return {"status": "ok"}
