from fastapi import APIRouter

from src.presentation.api.v1.sms.controllers.sms import router as sms_router

router = APIRouter(prefix="/v1")
router.include_router(sms_router, prefix="/sms", tags=["sms"])
