from fastapi import APIRouter, Depends, HTTPException

from app.helpers.login_manager import PermissionRequired
from app.schemas.sche_veterinary_clinic import VeterinaryClinicRequest
from app.services.srv_veterinary_clinic import VeterinaryClinicService

router = APIRouter()

@router.post('', dependencies=[Depends(PermissionRequired('admin'))])
def create_veterinarian(req: VeterinaryClinicRequest):
    exist_clinic = VeterinaryClinicService.is_exist_clinic(name=req.name)
    if exist_clinic:
        raise HTTPException(status_code=400, detail='Veterinary clinic is already exist')
    VeterinaryClinicService.create_clinic(data=req)
    return {
        'veterinary_clinic_id': VeterinaryClinicService.is_exist_clinic(name=req.name).get('id')
    }

@router.get('', dependencies=[Depends(PermissionRequired('admin'))])
def get_list_veterinary_clinics():
    return {
        'veterinary_clinics': VeterinaryClinicService.get_list_veterinary_clinics()
    }
