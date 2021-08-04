import logging
from datetime import date
from typing import Optional

from fastapi import APIRouter, Depends

from app.helpers.login_manager import PermissionRequired
from app.services.srv_sponsor import SponsorService

logger = logging.getLogger()
router = APIRouter()

@router.get('', dependencies=[Depends(PermissionRequired('admin', 'volunteer'))])
def get_list_donate_detail(start_at: Optional[date] = None, end_at: Optional[date] = None):
    return SponsorService.get_list_donate_detail(start_at=start_at, end_at=end_at)
