from fastapi import FastAPI, BackgroundTasks, UploadFile, File, Form
from starlette.responses import JSONResponse
from fastapi_mail import FastMail, MessageSchema
from app.schemas.sche_mail import EmailSchema, BodyEmail
from app.db.base import mail_config
from fastapi import APIRouter, Depends, HTTPException
from app.helpers.login_manager import PermissionRequired, login_required
import logging

logger = logging.getLogger()
router = APIRouter()


@router.post("", dependencies=[Depends(PermissionRequired('admin', 'volunteer'))])
async def send_mail(background_tasks: BackgroundTasks, email: EmailSchema, body_mail: BodyEmail) -> JSONResponse:
    message = MessageSchema(
        subject=body_mail.subject,
        recipients=email.dict().get("email"),
        body=body_mail.body
    )
    fm = FastMail(mail_config)
    background_tasks.add_task(fm.send_message, message)
    return JSONResponse(status_code=200, content={"message": "email has been sent"})
