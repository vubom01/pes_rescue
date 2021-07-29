from datetime import date

from pydantic import BaseModel


class WorkSchedule(BaseModel):
    working_day: date
    working_shift: int

class WorkingDay(BaseModel):
    working_day: date

class ConfirmWorkSchedule(BaseModel):
    working_day: date
    status: str
