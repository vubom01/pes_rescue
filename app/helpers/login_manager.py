from fastapi import Depends

from app.schemas.sche_user import UserItemResponse
from app.services.srv_user import UserService


def login_required(http_authorization_credentials=Depends(UserService().reusable_oauth2)):
    return UserService().get_current_user(http_authorization_credentials)


def permission(user: UserItemResponse = Depends(UserService.get_current_user)):
    role = UserService.is_exist_user(user['username'])['role']
    if role == 'guest':
        return True
    return False
