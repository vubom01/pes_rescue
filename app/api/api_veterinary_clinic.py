from fastapi import APIRouter, Depends, HTTPException

from app.helpers.login_manager import PermissionRequired
from app.schemas.sche_veterinary_clinic import VeterinaryClinicRequest
from app.services.srv_veterinary_clinic import VeterinaryClinicService

router = APIRouter()

@router.post('', dependencies=[Depends(PermissionRequired('admin'))])
def create_veterinarian(req: VeterinaryClinicRequest):
    if req.name is None:
        raise HTTPException(status_code=400, detail='name khong duoc de trong')
    if req.address is None:
        raise HTTPException(status_code=400, detail='address khong duoc de trong')
    if req.phone_number is None:
        raise HTTPException(status_code=400, detail='phone_number khong duoc de trong')
    if req.email is None:
        raise HTTPException(status_code=400, detail='email khong duoc de trong')

    exist_clinic = VeterinaryClinicService.is_exist_clinic(name=req.name)
    if exist_clinic:
        raise HTTPException(status_code=400, detail='Veterinary clinic is already exist')
    VeterinaryClinicService.create_clinic(data=req)
    return {
        'veterinary_clinic_id': VeterinaryClinicService.is_exist_clinic(name=req.name).get('id')
    }

@router.get('', dependencies=[Depends(PermissionRequired('admin', 'volunteer'))])
def get_list_veterinary_clinics():
    return {
        'veterinary_clinics': VeterinaryClinicService.get_list_veterinary_clinics()
    }

@router.get('/{id}', dependencies=[Depends(PermissionRequired('admin', 'volunteer'))])
def get_veterinary_clinic_detail(id: int):
    return VeterinaryClinicService.get_veterinary_clinic_detail(id=id)

@router.delete('/{id}', dependencies=[Depends(PermissionRequired('admin'))])
def delete_veterinary_clinic(id: int):
    return VeterinaryClinicService.delete_veterinary_clinic(id=id)
