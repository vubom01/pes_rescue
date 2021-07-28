import jwt
from fastapi import Depends, HTTPException
from fastapi.security import HTTPBearer
from pydantic import ValidationError
from starlette import status

from app.core.config import settings
from app.core.security import get_password_hash, verify_password
from app.db.base import mysql
from app.schemas.sche_token import TokenPayload
from app.schemas.sche_work_time import ConfirmWorkingTimeRequest


class WorkingTimeService(object):
    __instance = None

    reusable_oauth2 = HTTPBearer(
        scheme_name='Authorization'
    )

    @staticmethod
    def confirm_working_time(data: ConfirmWorkingTimeRequest):
        cursor = mysql.cursor()
        query = 'UPDATE work_schedule SET status = %s where user_id = %s and working_day = %s ;'
        cursor.execute(query, (data.status, data.user_id, data.working_day,))
        mysql.commit()