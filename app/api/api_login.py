from fastapi import APIRouter
from pydantic import BaseModel
from app.schemas.sche_base import Message
from app.services.srv_user import UserService

router = APIRouter()

class LoginRequest(BaseModel):
    username: str
    password: str

@router.post('', response_model=Message)
def login(request: LoginRequest):
    user = UserService.authentication(username=request.username, password=request.password)
    response = {
        'message': str,
        'status': bool
    }
    if user:
        response['message'] = 'Successful!'
        response['status'] = True
    else:
        response['message'] = 'Incorrect username/ password'
        response['status'] = False
    return response
