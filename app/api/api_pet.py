import logging

from fastapi import APIRouter, Depends, File, HTTPException, UploadFile
from starlette import status

from app.helpers.login_manager import PermissionRequired, login_required
from app.services.srv_pet import PetService

logger = logging.getLogger()
router = APIRouter()


@router.post('/images', dependencies=[Depends(PermissionRequired('admin'))])
def upload_pet_image(pet_id: int, file: UploadFile = File(...)):
    return PetService.upload_pet_image(pet_id=pet_id, image=file.file)

@router.post('', dependencies=[Depends(login_required)])
def get_list_pets():
    pets = PetService.get_list_pets()
    for pet in pets:
        images = PetService.get_pet_images(pet_id=pet.get('id'))
        pet['images'] = images
    return {
        'pets': pets
    }
