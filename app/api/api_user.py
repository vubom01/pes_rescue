import logging

from fastapi import APIRouter, Depends, HTTPException

from app.helpers.login_manager import login_required
from app.schemas.sche_user import UserItemResponse, UserUpdateRequest
from app.services.srv_user import UserService

logger = logging.getLogger()
router = APIRouter()

@router.get('/info', dependencies=[Depends(login_required)], response_model=UserItemResponse)
def detail_me(current_user: UserItemResponse = Depends(UserService().get_current_user)):
    return current_user

@router.put('/update',dependencies=[Depends(login_required)])
def update_info(request: UserUpdateRequest,user: UserItemResponse = Depends(UserService().get_current_user)):
    if request.first_name == None:
        request.first_name = user['first_name']
    if request.last_name == None:
        request.last_name = user['last_name']
    if request.email == None:
        request.email = user['emai']
    if request.phone_number == None:
        request.phone_number = user['phone_number']
    request.username = user['username']
    rowAffected = UserService.update_user_info(request)
    if rowAffected == 0:
        raise HTTPException(status_code=400, detail='Update failed')
    return {
        'message': 'Update success'
    }


