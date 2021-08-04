import logging
from datetime import date
from typing import Optional

from fastapi import APIRouter, Depends, HTTPException

from app.helpers.login_manager import PermissionRequired
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

@router.delete('/{id}', dependencies=[Depends(PermissionRequired('admin'))])
def delete_donate_detail(id: int):
    return SponsorService.delete_donate_detail(id=id)