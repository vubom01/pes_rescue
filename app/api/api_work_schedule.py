import logging

from fastapi import APIRouter, Depends, HTTPException

from app.helpers.login_manager import PermissionRequired
from app.schemas.sche_user import UserItemResponse
from app.schemas.sche_work_schedule import WorkSchedule, WorkingDay
from app.services.srv_user import UserService
from app.services.srv_work_schedule import WorkScheduleService

logger = logging.getLogger()
router = APIRouter()

@router.post('', dependencies=[Depends(PermissionRequired('volunteer'))])
def register_work_schedule(request: WorkSchedule,
                           current_user: UserItemResponse = Depends(UserService().get_current_user)):
    res = WorkScheduleService.is_exist_work_schedule(user_id=current_user.get('id'), working_day=request.working_day)
    if res:
        raise HTTPException(status_code=400, detail='You have registered up for the work schedule for this day')
    WorkScheduleService.register_work_schedule(user_id=current_user.get('id'), data=request)

@router.delete('', dependencies=[Depends(PermissionRequired('volunteer'))])
def delete_work_schedule(request: WorkingDay,
                         current_user: UserItemResponse = Depends(UserService().get_current_user)):
    WorkScheduleService.delete_work_schedule(user_id=current_user.get('id'), working_day=request.working_day)

@router.put('', dependencies=[Depends(PermissionRequired('volunteer'))])
def update_work_schedule(request: WorkSchedule,
                         current_user: UserItemResponse = Depends(UserService().get_current_user)):
    res = WorkScheduleService.is_exist_work_schedule(user_id=current_user.get('id'), working_day=request.working_day)
    if res is None:
        raise HTTPException(status_code=400, detail="You don't have registered up for the work schedule for this day")
    WorkScheduleService.update_work_schedule(user_id=current_user.get('id'), data=request)

