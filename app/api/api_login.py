from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

from app.core.security import create_access_token
from app.schemas.sche_token import Token
from app.services.srv_user import UserService

router = APIRouter()

class LoginRequest(BaseModel):
    username: str
    password: str

@router.post('', response_model=Token)
def login(request: LoginRequest):
    user = UserService.authentication(username=request.username, password=request.password)
    if not user:
        raise HTTPException(status_code=400, detail='Incorrect email or password')
    return Token(
        access_token=create_access_token(user_id=user['id'])
    )
