import logging

from fastapi import APIRouter, Depends, HTTPException

from app.helpers import login_manager
from app.helpers.login_manager import login_required
from app.schemas.sche_pet import PetInfoRequest
from app.schemas.sche_user import UserItemResponse
from app.services.srv_pet import PetService
from app.services.srv_user import UserService

logger = logging.getLogger()
router = APIRouter()


@router.post("/info", dependencies=[Depends(login_required)])
def create_pet_info(request: PetInfoRequest, current_user: UserItemResponse = Depends(UserService().get_current_user)):
    if login_manager.permission(current_user):
        raise HTTPException(status_code=403, detail="FORBIDDEN ACTION")
    exist_pet = PetService.is_exist_pet(name=request.name)
    if exist_pet:
        raise HTTPException(status_code=400, detail='Pet is already exist')
    PetService.pet_input_info(request)
    pet_id = PetService.is_exist_pet(name=request.name)['id']
    return {
        'pet_id': pet_id
    }
