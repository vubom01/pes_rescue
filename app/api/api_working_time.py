import logging

from fastapi import APIRouter, Depends

from app.helpers.login_manager import PermissionRequired, login_required
from app.schemas.sche_user import (ListUsers, UserItemResponse,
                                   UserUpdateRequest)
from app.schemas.sche_work_time import ConfirmWorkingTimeRequest
from app.services.srv_user import UserService
from app.services.srv_work_time import WorkingTimeService

logger = logging.getLogger()
router = APIRouter()


@router.put('/confirm/{user_id}', dependencies=[Depends(PermissionRequired("admin"))])
def register_working_time(data: ConfirmWorkingTimeRequest):
    return WorkingTimeService.confirm_working_time(data=data)
