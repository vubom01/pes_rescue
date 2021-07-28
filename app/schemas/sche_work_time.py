from typing import List, Optional
from datetime import date
from pydantic import BaseModel


class WorkingTimeRegisterRequest(BaseModel):
    user_id: int
    working_shift: int
    working_day: date
