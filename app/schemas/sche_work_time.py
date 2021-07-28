from typing import List, Optional
from datetime import date
from pydantic import BaseModel


class ConfirmWorkingTimeRequest(BaseModel):
    user_id: int
    working_day: date
    status: str
