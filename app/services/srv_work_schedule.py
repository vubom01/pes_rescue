from datetime import date

from app.db.base import mysql
from app.schemas.sche_work_schedule import WorkScheduleRegister, ConfirmWorkSchedule


class WorkScheduleService(object):

    @staticmethod
    def register_work_schedule(user_id: int, data: WorkScheduleRegister):
        cursor = mysql.cursor()
        query = 'insert into work_schedule (user_id, working_day, working_shift) values (%s, %s, %s)'
        cursor.execute(query, (user_id, data.working_day, data.working_shift))
        mysql.commit()

    @staticmethod
    def is_exist_work_schedule(user_id: int, working_day: date):
        cursor = mysql.cursor()
        query = 'select * from work_schedule where user_id = %s and working_day = %s'
        cursor.execute(query, (user_id, working_day,))
        res = cursor.fetchone()
        if not res:
            return None
        return res

    @staticmethod
    def confirm_work_schedule(user_id: int, data: ConfirmWorkSchedule):
        cursor = mysql.cursor()
        query = 'UPDATE work_schedule SET status = %s where user_id = %s and working_day = %s ;'
        cursor.execute(query, (data.status, user_id, data.working_day,))
        mysql.commit()
