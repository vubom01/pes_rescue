from fastapi import APIRouter, HTTPException

from app.schemas.sche_user import UserRegisterRequest
from app.services.srv_user import UserService

router = APIRouter()

@router.post('')
def register(request: UserRegisterRequest):
    exist_user = UserService.is_exist_user(username=request.username)
    if exist_user:
        raise HTTPException(status_code=400, detail='Username is already exist')
    UserService.register_user(data=request)
    user_id = UserService.is_exist_user(username=request.username)['id']
    return {
        'user_id': user_id
    }
