import logging
from datetime import date
from typing import Optional

from fastapi import APIRouter, Depends, HTTPException

from app.helpers.login_manager import PermissionRequired
from app.schemas.sche_sponsor import DonateDetailRequest
from app.services.srv_sponsor import SponsorService

logger = logging.getLogger()
router = APIRouter()

@router.get('', dependencies=[Depends(PermissionRequired('admin', 'volunteer'))])
def get_list_donate_detail(start_at: Optional[date] = None, end_at: Optional[date] = None):
    return SponsorService.get_list_donate_detail(start_at=start_at, end_at=end_at)

@router.get('/{id}', dependencies=[Depends(PermissionRequired('admin', 'volunteer'))])
def get_donate_detail_by_id(id: int):
    donate_detail = SponsorService.get_donate_detail_by_id(id=id)
    if donate_detail is None:
        raise HTTPException(status_code=400, detail='Donate detail not found')
    return donate_detail

@router.put('/{id}', dependencies=[Depends(PermissionRequired('admin', 'volunteer'))])
def update_donate_detail(id: int, req: DonateDetailRequest):
    donate_detail = SponsorService.get_donate_detail_by_id(id=id)
    if donate_detail is None:
        raise HTTPException(status_code=400, detail='Donate detail not found')

    if req.transaction_code:
        donate_detail = SponsorService.is_exist_donate_detail(transaction_code=req.transaction_code)
        if donate_detail:
            raise HTTPException(status_code=400, detail='Donate detail is already exist')

    if req.account_number is None:
        req.account_number = donate_detail.get('account_number')
    if req.transaction_code is None:
        req.transaction_code = donate_detail.get('transaction_code')
    if req.donations is None:
        req.donations = donate_detail.get('donations')

    return SponsorService.update_donate_detail(id=id, data=req)

@router.delete('/{id}', dependencies=[Depends(PermissionRequired('admin', 'volunteer'))])
def delete_donate_detail(id: int):
    return SponsorService.delete_donate_detail(id=id)
