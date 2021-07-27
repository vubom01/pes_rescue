import logging

from fastapi import APIRouter, Depends, File, HTTPException, UploadFile
from starlette import status

from app.helpers.login_manager import PermissionRequired, login_required
from app.services.srv_pet import PetService

logger = logging.getLogger()
router = APIRouter()


@router.post('/images', dependencies=[Depends(PermissionRequired('admin'))])
def upload_pet_image(pet_id: int, file: UploadFile = File(...)):
    data = file.file.read()
    if len(data) > 1024 * 1024 * 10:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"File too large",
        )
    file_name = " ".join(file.filename.strip().split())
    file_ext = file_name.split('.')[-1]
    if file_ext.lower() not in ('jpg', 'png', 'jpeg'):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Can't upload this file",
        )
    return PetService.upload_pet_image(pet_id=pet_id, image=file.file)
