import jwt
from fastapi import Depends, HTTPException
from fastapi.security import HTTPBearer
from pydantic import ValidationError
from starlette import status

from app.core.config import settings
from app.core.security import get_password_hash, verify_password
from app.db.base import mysql
from app.schemas.sche_token import TokenPayload
from app.schemas.sche_user import UserRegisterRequest, UserUpdateRequest


class UserService(object):
    __instance = None

    reusable_oauth2 = HTTPBearer(
        scheme_name='Authorization'
    )

    @staticmethod
    def authentication(username: str, password: str):
        cursor = mysql.cursor()
        query = 'select * from users where username = %s'
        cursor.execute(query, (username,))
        user = cursor.fetchone()
        if not user:
            return None
        if not verify_password(password, user['password']):
            return None
        return user

    @staticmethod
    def get_current_user(http_authorization_credentials=Depends(reusable_oauth2)):
        try:
            payload = jwt.decode(
                http_authorization_credentials.credentials, settings.SECRET_KEY,
                algorithms=[settings.SECURITY_ALGORITHM]
            )
            token_data = TokenPayload(**payload)
        except(jwt.PyJWTError, ValidationError):
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail=f"Could not validate credentials",
            )
        cursor = mysql.cursor()
        query = 'select * from users where id = %s'
        cursor.execute(query, token_data.user_id,)
        user = cursor.fetchone()
        if not user:
            raise HTTPException(status_code=404, detail="User not found")
        return user

    @staticmethod
    def is_exist_user(username: str):
        cursor = mysql.cursor()
        query = 'select * from users where username = %s'
        cursor.execute(query, (username,))
        user = cursor.fetchone()
        if not user:
            return None
        return user

    @staticmethod
    def register_user(data=UserRegisterRequest):
        cursor = mysql.cursor()
        query = 'insert into users (username, password, first_name, last_name, email, phone_number) ' \
                'values (%s, %s, %s, %s, %s, %s)'
        cursor.execute(query, (data.username, get_password_hash(data.password), data.first_name, data.last_name,
                               data.email, data.phone_number,))
        mysql.commit()

    @staticmethod
    def update_user_info(data=UserUpdateRequest):
        cursor = mysql.cursor()
        query = 'update users set first_name = %s, last_name = %s, email = %s, phone_number = %s where username = %s'
        cursor.execute(query, (data.first_name, data.last_name, data.email, data.phone_number,data.username,))
        mysql.commit()
        return cursor.rowcount
