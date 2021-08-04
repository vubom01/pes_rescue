import logging
from typing import List, Optional

from fastapi import APIRouter, Depends
from fastapi_mail import FastMail, MessageSchema
from pydantic import BaseModel, EmailStr

from app.db.base import mail_config
from app.helpers.login_manager import PermissionRequired

logger = logging.getLogger()
router = APIRouter()

class BodyEmail(BaseModel):
    subject: Optional[str]
    body: str

@router.post('', dependencies=[Depends(PermissionRequired('admin', 'volunteer'))])
async def send_mail(email: List[EmailStr], body_mail: BodyEmail):
    message = MessageSchema(
        subject=body_mail.subject,
        recipients=email,
        body=body_mail.body
    )
    fm = FastMail(mail_config)
    await fm.send_message(message)
    return {
        'message': 'email has been sent'
    }
