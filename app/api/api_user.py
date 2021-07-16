import logging

from fastapi import APIRouter, Depends

from app.helpers.login_manager import login_required
from app.schemas.sche_user import UserItemResponse, UserUpdateRequest
from app.services.srv_user import UserService

logger = logging.getLogger()
router = APIRouter()

@router.get('/info', dependencies=[Depends(login_required)], response_model=UserItemResponse)
def detail_me(current_user: UserItemResponse = Depends(UserService().get_current_user)):
    return current_user

@router.put('/info', dependencies=[Depends(login_required)])
def update_me(request: UserUpdateRequest, current_user: UserItemResponse = Depends(UserService().get_current_user)):
    if request.first_name is None:
        request.first_name = current_user['first_name']
    if request.last_name is None:
        request.last_name = current_user['last_name']
    if request.email is None:
        request.email = current_user['email']
    if request.phone_number is None:
        request.phone_number = current_user['phone_number']
    UserService.update_current_user(data=request, id=current_user['id'])


