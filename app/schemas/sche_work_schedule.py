from datetime import date
from typing import List, Optional

from pydantic import BaseModel


class WorkSchedule(BaseModel):
    working_day: date
    working_shift: Optional[int]

class ListWorkSchedule(BaseModel):
    work_schedule: List[WorkSchedule]

class WorkingDay(BaseModel):
    working_day: date

class ConfirmWorkSchedule(BaseModel):
    working_day: date
    status: str
