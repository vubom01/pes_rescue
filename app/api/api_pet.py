import logging

from fastapi import APIRouter, Depends, File, HTTPException, UploadFile
from starlette import status

from app.helpers.login_manager import PermissionRequired, login_required
from app.schemas.sche_pet import ListPets
from app.services.srv_pet import PetService

logger = logging.getLogger()
router = APIRouter()


@router.post('/images', dependencies=[Depends(PermissionRequired('admin'))])
def upload_pet_image(pet_id: int, file: UploadFile = File(...)):
    return PetService.upload_pet_image(pet_id=pet_id, image=file.file)


