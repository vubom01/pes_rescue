import logging
from datetime import date
from typing import Optional

from fastapi import APIRouter, Depends, HTTPException

from app.helpers.login_manager import PermissionRequired
from app.schemas.sche_user import UserItemResponse
from app.schemas.sche_work_schedule import (ConfirmWorkSchedule, WorkingDay,
                                            WorkSchedule)
from app.services.srv_user import UserService
from app.services.srv_work_schedule import WorkScheduleService

logger = logging.getLogger()
router = APIRouter()

@router.post('/me', dependencies=[Depends(PermissionRequired('volunteer'))])
def register_work_schedule(request: WorkSchedule,
                           current_user: UserItemResponse = Depends(UserService().get_current_user)):
    res = WorkScheduleService.is_exist_work_schedule(user_id=current_user.get('id'), working_day=request.working_day)
    if res:
        raise HTTPException(status_code=400, detail='You have registered up for the work schedule for this day')
    if request.working_shift != 0 and request.working_shift != 1 and request.working_shift != 2:
        raise HTTPException(status_code=400, detail='work_shift chỉ nhận các giá trị 0, 1, 2')
    WorkScheduleService.register_work_schedule(user_id=current_user.get('id'), data=request)

@router.delete('/me', dependencies=[Depends(PermissionRequired('volunteer'))])
def delete_work_schedule(request: WorkingDay,
                         current_user: UserItemResponse = Depends(UserService().get_current_user)):
    WorkScheduleService.delete_work_schedule(user_id=current_user.get('id'), working_day=request.working_day)

@router.put('/me', dependencies=[Depends(PermissionRequired('volunteer'))])
def update_work_schedule(request: WorkSchedule,
                         current_user: UserItemResponse = Depends(UserService().get_current_user)):
    res = WorkScheduleService.is_exist_work_schedule(user_id=current_user.get('id'), working_day=request.working_day)
    if res is None:
        raise HTTPException(status_code=400, detail="You don't have registered up for the work schedule for this day")
    if request.working_shift != 0 and request.working_shift != 1 and request.working_shift != 2:
        raise HTTPException(status_code=400, detail='work_shift chỉ nhận các giá trị 0, 1, 2')
    WorkScheduleService.update_work_schedule(user_id=current_user.get('id'), data=request)

@router.get('', dependencies=[Depends(PermissionRequired('admin', 'volunteer'))])
def get_list_work_schedule(start_at: Optional[date] = None, end_at: Optional[date] = None):
    list_users = UserService.get_list_users_by_role(role='volunteer')
    users = []
    for user in list_users:
        u = WorkScheduleService.get_user_work_schedule(user_id=user.get('id'), start_at=start_at, end_at=end_at)
        if u.get('id') is None:
            u['id'] = user.get('id')
            u['full_name'] = user.get('first_name') + ' ' + user.get('last_name')
            u['total_shift'] = 0
        users.append(u)
    return {
        'users': users
    }

@router.get('/{user_id}', dependencies=[Depends(PermissionRequired('admin', 'volunteer'))])
def get_work_schedule_by_user_id(user_id: int, start_at: Optional[date] = None, end_at: Optional[date] = None):
    check_user = UserService.get_user_by_id(user_id=user_id)
    if check_user.get('role') != 'volunteer':
        raise HTTPException(status_code=400, detail="User is not volunteer")
    user = WorkScheduleService.get_user_work_schedule(user_id=user_id, start_at=start_at, end_at=end_at)
    if user.get('id') is None:
        user['id'] = check_user.get('id')
        user['full_name'] = check_user.get('first_name') + ' ' + check_user.get('last_name')
        user['total_shift'] = 0
    user['work_schedule'] = WorkScheduleService.get_list_work_schedule_by_user_id(user_id=user_id,
                                                                                  start_at=start_at, end_at=end_at)
    return user

@router.put('/{user_id}', dependencies=[Depends(PermissionRequired("admin"))])
def confirm_work_schedule(user_id: int, data: ConfirmWorkSchedule):
    user = UserService.get_user_by_id(user_id=user_id)
    if user.get('role') != 'volunteer':
        raise HTTPException(status_code=400, detail="User is not volunteer")
    return WorkScheduleService.confirm_work_schedule(user_id=user_id, data=data)
