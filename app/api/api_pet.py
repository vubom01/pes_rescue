import logging
from typing import List

from fastapi import APIRouter, Depends, File, Form, HTTPException, UploadFile

from app.helpers.login_manager import PermissionRequired, login_required
from app.services.srv_pet import PetService

logger = logging.getLogger()
router = APIRouter()


@router.post('/images', dependencies=[Depends(PermissionRequired('admin'))])
def upload_pet_image(pet_id: int, file: UploadFile = File(...)):
    file_name = " ".join(file.filename.strip().split())
    file_ext = file_name.split('.')[-1]
    if file_ext.lower() not in ('jpg', 'png', 'jpeg'):
        raise HTTPException(status_code=400, detail='Can not upload file ' + file.filename)
    return PetService.upload_pet_image(pet_id=pet_id, image=file.file)

@router.post('', dependencies=[Depends(PermissionRequired('admin'))])
def create_pet(name: str = Form(...),
               age: int = Form(...),
               color: str = Form(...),
               health_condition: str = Form(...),
               weight: float = Form(...),
               description: str = Form(...),
               species: str = Form(...),
               images: List[UploadFile] = File(...)):
    exist_pet = PetService.is_exist_pet(name=name)
    if exist_pet:
        raise HTTPException(status_code=400, detail='Pet name is already exist')
    PetService.create_pet(name=name, age=age, color=color, health_condition=health_condition, weight=weight,
                          description=description, species=species)
    pet_id = PetService.is_exist_pet(name=name)['id']
    for image in images:
        upload_pet_image(pet_id=pet_id, file=image)
    return {
        "pet_id": pet_id
    }
@router.get('', dependencies=[Depends(login_required)])
def get_list_pets():
    pets = PetService.get_list_pets()
    for pet in pets:
        images = PetService.get_pet_images(pet_id=pet.get('id'))
        pet['images'] = images
    return {
        'pets': pets
    }
