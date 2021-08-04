from datetime import date
from typing import Optional

from pydantic import BaseModel


class VeterinaryClinicRequest(BaseModel):
    name: Optional[str]
    address: Optional[str]
    phone_number: Optional[str]
    email: Optional[str]


class HealthyReportRequest(BaseModel):
    start_at: date
    end_at: date


class HealthReportResponse(BaseModel):
    pet_id: int
    created_at: date
    veterinary_clinic_id: int
    health_condition: str
    weight: float
    description: str
