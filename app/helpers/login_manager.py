from fastapi import Depends

from app.services.srv_user import UserService


def login_required(http_authorization_credentials=Depends(UserService().reusable_oauth2)):
    return UserService().get_current_user(http_authorization_credentials)
