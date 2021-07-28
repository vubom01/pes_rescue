import jwt
from fastapi import Depends, HTTPException
from fastapi.security import HTTPBearer
from pydantic import ValidationError
from starlette import status

from app.core.config import settings
from app.core.security import get_password_hash, verify_password
from app.db.base import mysql
from app.schemas.sche_token import TokenPayload
from app.schemas.sche_work_time import WorkingTimeRegisterRequest


class WorkingTimeService(object):
    __instance = None

    reusable_oauth2 = HTTPBearer(
        scheme_name='Authorization'
    )

    @staticmethod
    def register_work_time(data: WorkingTimeRegisterRequest):
        cursor = mysql.cursor()
        working_day = str(data.working_day.year) + "-" + str(data.working_day.month) + "-" + str(data.working_day.day)
        print(working_day)
        query = 'insert into work_schedule (user_id, working_shift, working_day) values (%s, %s,%s);'
        cursor.execute(query, (data.user_id, data.working_shift, working_day,))
        mysql.commit()
