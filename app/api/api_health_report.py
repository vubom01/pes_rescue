import logging

from fastapi import APIRouter, Depends, HTTPException

from app.helpers.login_manager import PermissionRequired
from app.schemas.sche_veterinary_clinic import HealthReportRequest
from app.services.srv_pet import PetService
from app.services.srv_veterinary_clinic import VeterinaryClinicService

logger = logging.getLogger()
router = APIRouter()

@router.post('', dependencies=[Depends(PermissionRequired('admin'))])
def create_health_report(req: HealthReportRequest):
    if req.pet_id is None:
        raise HTTPException(status_code=400, detail='pet_id khong duoc de trong')
    if req.veterinary_clinic_id is None:
        raise HTTPException(status_code=400, detail='veterinary_clinic_id khong duoc de trong')
    if req.weight is None:
        raise HTTPException(status_code=400, detail='weight khong duoc de trong')
    if req.health_condition is None:
        raise HTTPException(status_code=400, detail='health_condition khong duoc de trong')
    if req.description is None:
        raise HTTPException(status_code=400, detail='description khong duoc de trong')

    pet = PetService.get_pet_by_id(pet_id=req.pet_id)
    if pet is None:
        raise HTTPException(status_code=400, detail='Pet not found')

    clinic = VeterinaryClinicService.get_veterinary_clinic_detail(id=req.veterinary_clinic_id)
    if clinic is None:
        raise HTTPException(status_code=400, detail='Veterinary clinic not found')

    return VeterinaryClinicService.create_health_report(data=req)




