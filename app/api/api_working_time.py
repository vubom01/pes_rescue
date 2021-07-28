import logging

from fastapi import APIRouter, Depends

from app.helpers.login_manager import PermissionRequired, login_required
from app.schemas.sche_user import (ListUsers, UserItemResponse,
                                   UserUpdateRequest)
from app.schemas.sche_work_time import WorkingTimeRegisterRequest
from app.services.srv_user import UserService
from app.services.srv_work_time import WorkingTimeService

logger = logging.getLogger()
router = APIRouter()


@router.post('/{user_id}', dependencies=[Depends(PermissionRequired("volunteer"))])
def register_working_time(data: WorkingTimeRegisterRequest):
    return WorkingTimeService.register_work_time(data=data)
