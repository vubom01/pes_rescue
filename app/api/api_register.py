from fastapi import APIRouter
from app.schemas.sche_user import UserRegisterRequest
from app.services.srv_user import UserService

router = APIRouter()

@router.post('')
def login(request: UserRegisterRequest):
    exist_user = UserService.is_exist_user(username=request.username)
    if exist_user:
        raise Exception('username already exists')
    UserService.register_user(data=request)
    user_id = UserService.is_exist_user(username=request.username)['id']
    return user_id
