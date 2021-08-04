import logging
from datetime import date
from typing import List, Optional

from fastapi import APIRouter, Depends, File, HTTPException, UploadFile

from app.helpers.login_manager import PermissionRequired
from app.schemas.sche_pet import PetInfoRequest, Url
from app.services.srv_pet import PetService
from app.services.srv_veterinary_clinic import VeterinaryClinicService

logger = logging.getLogger()
router = APIRouter()


@router.post('', dependencies=[Depends(PermissionRequired('admin'))])
def create_pet(pet_info: PetInfoRequest):
    if pet_info.name is None:
        raise HTTPException(status_code=400, detail='name khong duoc de trong')
    if pet_info.age is None:
        raise HTTPException(status_code=400, detail='age khong duoc de trong')
    if pet_info.color is None:
        raise HTTPException(status_code=400, detail='color khong duoc de trong')
    if pet_info.health_condition is None:
        raise HTTPException(status_code=400, detail='health_condition khong duoc de trong')
    if pet_info.weight is None:
        raise HTTPException(status_code=400, detail='weight khong duoc de trong')
    if pet_info.species is None:
        raise HTTPException(status_code=400, detail='species khong duoc de trong')
    if pet_info.gender is None:
        raise HTTPException(status_code=400, detail='gender khong duoc de trong')

    exist_pet = PetService.is_exist_pet(name=pet_info.name)
    if exist_pet:
        raise HTTPException(status_code=400, detail='Pet name is already exist')

    if pet_info.species != 'cat' and pet_info.species != 'dog':
        raise HTTPException(status_code=400, detail='species chỉ nhận các giá trị cat, dog')
    if pet_info.age != 'young' and pet_info.age != 'mature' and pet_info.age != 'old':
        raise HTTPException(status_code=400, detail='age chỉ nhận các giá trị young, mature, old')
    if pet_info.gender != 'male' and pet_info.gender != 'female':
        raise HTTPException(status_code=400, detail='gender chỉ nhận các giá trị male, female')

    PetService.create_pet(data=pet_info)
    pet_id = PetService.is_exist_pet(name=pet_info.name)['id']
    return {
        "pet_id": pet_id
    }

@router.get('')
def get_list_pets(species: Optional[str] = None, age: Optional[str] = None, gender: Optional[str] = None):
    pets = PetService.get_list_pets(species=species, age=age, gender=gender)
    for pet in pets:
        images = PetService.get_pet_images(pet_id=pet.get('id'))
        pet['images'] = images
    return {
        'pets': pets
    }

@router.get('/{pet_id}')
def get_pet_by_id(pet_id: int):
    pet = PetService.get_pet_by_id(pet_id=pet_id)
    if pet is None:
        raise HTTPException(status_code=400, detail='Pet not found')
    pet['images'] = PetService.get_pet_images(pet_id=pet_id)
    return pet

@router.put('/{pet_id}', dependencies=[Depends(PermissionRequired('admin'))])
def update_pet_info(pet_id: int, pet_info: PetInfoRequest):
    pet = get_pet_by_id(pet_id=pet_id)

    if pet_info.name is None:
        pet_info.name = pet.get('name')
    else:
        exist_pet = PetService.is_exist_pet(name=pet_info.name)
        if exist_pet:
            raise HTTPException(status_code=400, detail='Pet name is already exist')

    if pet_info.age is None:
        pet_info.age = pet.get('age')
    if pet_info.color is None:
        pet_info.color = pet.get('color')
    if pet_info.health_condition is None:
        pet_info.health_condition = pet.get('health_condition')
    if pet_info.weight is None:
        pet_info.weight = pet.get('weight')
    if pet_info.description is None:
        pet_info.description = pet.get('description')
    if pet_info.species is None:
        pet_info.species = pet.get('species')

    if pet_info.species != 'dog' and pet_info.species != 'cat':
        raise HTTPException(status_code=400, detail='species chỉ nhận các giá trị cat, dog')
    if pet_info.age != 'young' and pet_info.age != 'mature' and pet_info.age != 'old':
        raise HTTPException(status_code=400, detail='age chỉ nhận các giá trị young, mature, old')
    if pet_info.gender != 'male' and pet_info.gender != 'female':
        raise HTTPException(status_code=400, detail='gender chỉ nhận các giá trị male, female')

    PetService.update_pet_info(pet_id=pet_id, data=pet_info)

@router.post('/{pet_id}/images', dependencies=[Depends(PermissionRequired('admin'))])
def upload_list_pet_images(pet_id: int, images: List[UploadFile] = File(...)):
    get_pet_by_id(pet_id=pet_id)
    urls = []
    for image in images:
        file_name = " ".join(image.filename.strip().split())
        file_ext = file_name.split('.')[-1]
        if file_ext.lower() not in ('jpg', 'png', 'jpeg'):
            raise HTTPException(status_code=400, detail='Can not upload file ' + image.filename)
        urls.append(PetService.upload_pet_image(pet_id=pet_id, image=image.file))
    return {
        'urls': urls
    }

@router.delete('/{pet_id}/images', dependencies=[Depends(PermissionRequired('admin'))])
def delete_image(pet_id: int, req: Url):
    PetService.delete_image(pet_id=pet_id, url=req.url)

@router.get('/{pet_id}/health_report', dependencies=[Depends(PermissionRequired('admin','volunteer'))])
def get_list_health_report_of_pet(pet_id: int, start_at: Optional[date] = None, end_at: Optional[date] = None):
    pet = PetService.get_pet_by_id(pet_id=pet_id)
    if pet is None:
        raise HTTPException(status_code=400, detail='Pet not found')
    return {
        'health_reports':
            VeterinaryClinicService.get_list_health_reports_by_pet_id_or_veterinary_clinic_id(pet_id=pet_id,
                                                                                              veterinary_clinic_id=None,
                                                                                              start_at=start_at,
                                                                                              end_at=end_at)
    }
