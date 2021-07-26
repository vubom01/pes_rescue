from fastapi import Depends, HTTPException

from app.schemas.sche_user import UserItemResponse
from app.services.srv_user import UserService


def login_required(http_authorization_credentials=Depends(UserService().reusable_oauth2)):
    return UserService().get_current_user(http_authorization_credentials)

class PermissionRequired:
    def __init__(self, *args):
        self.user = None
        self.permissions = args

    def __call__(self, current_user: UserItemResponse = Depends(login_required)):
        self.user = current_user
        if self.user.get('role') not in self.permissions and self.permissions:
            raise HTTPException(status_code=400,
                                detail=f'User ' + self.user.get('username') + f' can not access this api')
