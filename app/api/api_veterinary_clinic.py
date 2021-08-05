import logging
from datetime import date
from typing import Optional

from fastapi import APIRouter, Depends, HTTPException

from app.helpers.login_manager import PermissionRequired
from app.schemas.sche_veterinary_clinic import VeterinaryClinicRequest
from app.services.srv_veterinary_clinic import VeterinaryClinicService

logger = logging.getLogger()
router = APIRouter()

@router.post('', dependencies=[Depends(PermissionRequired('admin', 'volunteer'))])
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
    clinic = VeterinaryClinicService.get_veterinary_clinic_detail(id=id)
    if clinic is None:
        raise HTTPException(status_code=400, detail='Veterinary clinic not found')
    return clinic

@router.delete('/{id}', dependencies=[Depends(PermissionRequired('admin', 'volunteer'))])
def delete_veterinary_clinic(id: int):
    return VeterinaryClinicService.delete_veterinary_clinic(id=id)

@router.put('/{id}', dependencies=[Depends(PermissionRequired('admin', 'volunteer'))])
def update_veterinary_clinic(id: int, req: VeterinaryClinicRequest):
    clinic = VeterinaryClinicService.get_veterinary_clinic_detail(id=id)
    if clinic is None:
        raise HTTPException(status_code=400, detail='Veterinary clinic not found')

    if req.name is None:
        req.name = clinic.get('name')
    else:
        exist_clinic = VeterinaryClinicService.is_exist_clinic(name=req.name)
        if exist_clinic:
            raise HTTPException(status_code=400, detail='Veterinary clinic already exist')

    if req.name is None:
        req.name = clinic.get('name')
    if req.address is None:
        req.address = clinic.get('address')
    if req.phone_number is None:
        req.phone_number = clinic.get('phone_number')
    if req.email is None:
        req.email = clinic.get('email')

    return VeterinaryClinicService.update_veterinary_clinic(id=id, data=req)

@router.get("/{id}/health_report", dependencies=[Depends(PermissionRequired('admin', 'volunteer'))])
def get_list_healthy_reports_of_veterinary_clinic(id: int, start_at: Optional[date] = None,
                                                  end_at: Optional[date] = None):
    clinic = VeterinaryClinicService.get_veterinary_clinic_detail(id=id)
    if clinic is None:
        raise HTTPException(status_code=400, detail='Veterinary clinic not found')
    return {
        'health_reports':
            VeterinaryClinicService.get_list_health_reports_by_pet_id_or_veterinary_clinic_id(pet_id=None,
                                                                                              veterinary_clinic_id=id,
                                                                                              start_at=start_at,
                                                                                              end_at=end_at)
    }
