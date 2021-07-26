import logging

from fastapi import APIRouter, Depends

from app.helpers.login_manager import login_required, PermissionRequired
from app.schemas.sche_user import UserItemResponse, UserUpdateRequest, ListUsers
from app.helpers.login_manager import login_required
from app.schemas.sche_user import UserItemResponse, UserUpdateRequest, UpdatePermissionRequest
from app.services.srv_user import UserService

logger = logging.getLogger()
router = APIRouter()

@router.get('/me', dependencies=[Depends(login_required)], response_model=UserItemResponse)
def detail_me(current_user: UserItemResponse = Depends(UserService().get_current_user)):
    return current_user

@router.put('/me', dependencies=[Depends(login_required)])
def update_me(request: UserUpdateRequest, current_user: UserItemResponse = Depends(UserService().get_current_user)):
    UserService.update_current_user(data=request, current_user=current_user)

@router.get('', dependencies=[Depends(login_required)], response_model=ListUsers)
def get_list_users():
    users = UserService.get_list_users()
    return {
        'users': users
    }

@router.put('/{user_id}', dependencies=[Depends(login_required)])
def update_permission(request: UpdatePermissionRequest,
                      current_user: UserItemResponse = Depends(UserService().get_current_user)):
    UserService.update_permission(data=request, current_user=current_user)
