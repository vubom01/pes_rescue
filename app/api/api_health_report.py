import logging
from datetime import date
from typing import Optional

from fastapi import APIRouter, Depends, HTTPException

from app.helpers.login_manager import PermissionRequired
from app.schemas.sche_veterinary_clinic import HealthReportRequest
from app.services.srv_pet import PetService
from app.services.srv_veterinary_clinic import VeterinaryClinicService

logger = logging.getLogger()
router = APIRouter()

@router.post('', dependencies=[Depends(PermissionRequired('admin', 'volunteer'))])
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

@router.get('', dependencies=[Depends(PermissionRequired('admin', 'volunteer'))])
def get_list_health_report(start_at: Optional[date] = None, end_at: Optional[date] = None):
    return {
        'health_reports': VeterinaryClinicService.get_list_health_reports(start_at=start_at, end_at=end_at)
    }

@router.get('/{id}', dependencies=[Depends(PermissionRequired('admin', 'volunteer'))])
def get_health_report_detail(id: int):
    health_report = VeterinaryClinicService.get_health_report_detail(id=id)
    if health_report is None:
        raise HTTPException(status_code=400, detail='Health report not found')
    return health_report

@router.put('/{id}', dependencies=[Depends(PermissionRequired('admin', 'volunteer'))])
def update_health_report(id: int, req: HealthReportRequest):
    health_report = VeterinaryClinicService.get_health_report_detail(id=id)
    if health_report is None:
        raise HTTPException(status_code=400, detail='Health report not found')

    if req.pet_id is None:
        req.pet_id = health_report.get('pet_id')
    else:
        pet = PetService.get_pet_by_id(pet_id=req.pet_id)
        if pet is None:
            raise HTTPException(status_code=400, detail='Pet not found')

    if req.veterinary_clinic_id is None:
        req.veterinary_clinic_id = health_report.get('veterinary_clinic_id')
    else:
        clinic = VeterinaryClinicService.get_veterinary_clinic_detail(id=req.veterinary_clinic_id)
        if clinic is None:
            raise HTTPException(status_code=400, detail='Veterinary clinic not found')

    if req.weight is None:
        req.weight = health_report.get('weight')
    if req.health_condition is None:
        req.health_condition = health_report.get('health_condition')
    if req.description is None:
        req.description = health_report.get('description')

    return VeterinaryClinicService.update_health_report(id=id, data=req)

@router.delete('/{id}', dependencies=[Depends(PermissionRequired('admin', 'volunteer'))])
def delete_health_report(id: int):
    return VeterinaryClinicService.delete_health_report(id=id)