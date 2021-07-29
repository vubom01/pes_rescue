import logging

from fastapi import APIRouter, Depends
from pydantic import BaseModel

from app.helpers.login_manager import PermissionRequired, login_required
from app.schemas.sche_user import (ListUsers, Role, UserItemResponse,
                                   UserUpdateRequest)
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

@router.get('/volunteers', dependencies=[Depends(login_required)], response_model=ListUsers)
def get_list_volunteers():
    users = UserService.get_list_volunteers()
    return {
        'users': users
    }

@router.get('/{user_id}', dependencies=[Depends(login_required)], response_model=UserItemResponse)
def get_user_by_id(user_id: int):
    return UserService.get_user_by_id(user_id=user_id)

@router.put('/{user_id}/role', dependencies=[Depends(PermissionRequired('admin'))])
def update_user_role(user_id: int, req: Role):
    UserService.update_user_role(user_id=user_id, role=req.role)
