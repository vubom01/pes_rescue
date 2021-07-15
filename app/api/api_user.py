import logging
from fastapi import APIRouter, Depends
from app.helpers.login_manager import login_required
from app.schemas.sche_user import UserItemResponse
from app.services.srv_user import UserService

logger = logging.getLogger()
router = APIRouter()

@router.get("/me", dependencies=[Depends(login_required)], response_model=UserItemResponse)
def detail_me(current_user: UserItemResponse = Depends(UserService().get_current_user)):
    return current_user

