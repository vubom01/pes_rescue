from fastapi import APIRouter, Depends, HTTPException

from app.helpers.login_manager import PermissionRequired
from app.schemas.sche_sponsor import SponsorRequest
from app.services.srv_sponsor import SponsorService

router = APIRouter()


@router.post('', dependencies=[Depends(PermissionRequired('admin'))])
def create_sponsor(req: SponsorRequest):
    if req.first_name is None:
        raise HTTPException(status_code=400, detail='first_name khong duoc de trong')
    if req.last_name is None:
        raise HTTPException(status_code=400, detail='last_name khong duoc de trong')
    if req.address is None:
        raise HTTPException(status_code=400, detail='address khong duoc de trong')
    if req.email is None:
        raise HTTPException(status_code=400, detail='email khong duoc de trong')
    if req.phone_number is None:
        raise HTTPException(status_code=400, detail='phone_number khong duoc de trong')

    exist_sponsor = SponsorService.is_exist_sponsor(email=req.email, phone_number=req.phone_number).get('id')
    if exist_sponsor:
        raise HTTPException(status_code=400, detail='Sponsor is already exist')
    SponsorService.create_sponsor(data=req)
    return {
        'sponsor_id': SponsorService.is_exist_sponsor(email=req.email, phone_number=req.phone_number).get('id')
    }

@router.get('', dependencies=[Depends(PermissionRequired('admin', 'volunteer'))])
def get_list_sponsors():
    return {
        'sponsors': SponsorService.get_list_sponsors()
    }

@router.get('/{id}', dependencies=[Depends(PermissionRequired('admin', 'volunteer'))])
def get_sponsor_detail(id: int):
    sponsor = SponsorService.get_sponsor_detail(id=id)
    if sponsor is None:
        raise HTTPException(status_code=400, detail='Sponsor not found')
    return sponsor

@router.delete('/{id}', dependencies=[Depends(PermissionRequired('admin'))])
def delete_sponsor(id: int):
    return SponsorService.delete_sponsor(id=id)

@router.put('/{id}', dependencies=[Depends(PermissionRequired('admin'))])
def update_info_sponsor(id: int, req: SponsorRequest):
    exist_sponsor = SponsorService.is_exist_sponsor(email=req.email, phone_number=req.phone_number)
    if exist_sponsor:
        raise HTTPException(status_code=400, detail='sponsor already exist')
    sponsor = SponsorService.get_sponsor_detail(id=id)
    if sponsor is None:
        raise HTTPException(status_code=400, detail='Sponsor not found')

    if req.first_name is None:
        req.first_name = sponsor.get('first_name')
    if req.last_name is None:
        req.last_name = sponsor.get('last_name')
    if req.address is None:
        req.address = sponsor.get('address')
    if req.phone_number is None:
        req.phone_number = sponsor.get('phone_number')
    if req.email is None:
        req.email = sponsor.get('email')

    return SponsorService.update_info_sponsor(id=id, data=req)
