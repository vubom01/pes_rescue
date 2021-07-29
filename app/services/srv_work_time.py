import jwt
from fastapi import Depends, HTTPException
from fastapi.security import HTTPBearer
from pydantic import ValidationError
from starlette import status

from app.core.config import settings
from app.core.security import get_password_hash, verify_password
from app.db.base import mysql
from app.schemas.sche_token import TokenPayload
from app.schemas.sche_work_time import WorkingTimeRequest


class WorkingTimeService(object):
    __instance = None

    reusable_oauth2 = HTTPBearer(
        scheme_name='Authorization'
    )

    @staticmethod
    def update_working_time(data: WorkingTimeRequest, shift: int):
        cursor = mysql.cursor()
        query = 'UPDATE work_schedule SET working_shift = %s where user_id = %s and working_day = %s ;'
        cursor.execute(query, (shift, data.user_id, data.working_day,))
        mysql.commit()

    @staticmethod
    def delete_working_time(data: WorkingTimeRequest):
        cursor = mysql.cursor()
        query = 'DELETE FROM work_schedule  where user_id = %s and working_day = %s ;'
        cursor.execute(query, (data.user_id, data.working_day,))
        mysql.commit()
