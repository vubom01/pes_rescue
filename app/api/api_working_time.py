import logging

from fastapi import APIRouter, Depends
from app.helpers.login_manager import PermissionRequired
from app.schemas.sche_work_time import WorkingTimeRequest
from app.services.srv_work_time import WorkingTimeService

logger = logging.getLogger()
router = APIRouter()


@router.put('/working_time/{user_id}', dependencies=[Depends(PermissionRequired("volunteer"))])
def update_working_time(data: WorkingTimeRequest, shift: int):
    return WorkingTimeService.update_working_time(data=data, shift=shift)


@router.delete('/working_time/{user_id}', dependencies=[Depends(PermissionRequired("volunteer"))])
def delete_working_time(data: WorkingTimeRequest):
    return WorkingTimeService.delete_working_time(data=data)
