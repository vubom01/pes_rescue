import logging

from fastapi import APIRouter, Depends, File, HTTPException, UploadFile
from starlette import status

from app.helpers.login_manager import PermissionRequired, login_required
from app.schemas.sche_pet import PetItemResponse
from app.services.srv_pet import PetService

logger = logging.getLogger()
router = APIRouter()


@router.post('/images', dependencies=[Depends(PermissionRequired('admin'))])
def upload_pet_image(pet_id: int, file: UploadFile = File(...)):
    file_name = " ".join(file.filename.strip().split())
    file_ext = file_name.split('.')[-1]
    if file_ext.lower() not in ('jpg', 'png', 'jpeg'):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Can't upload this file",
        )
    return PetService.upload_pet_image(pet_id=pet_id, image=file.file)


@router.get('/{pet_id}', dependencies=[Depends(login_required)], response_model=PetItemResponse)
def get_pet_by_id(pet_id: int):
    return PetService.get_pet_by_id(pet_id=pet_id)
