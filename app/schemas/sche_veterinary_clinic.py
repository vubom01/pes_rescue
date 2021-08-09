from datetime import date
from typing import List, Optional

from pydantic import BaseModel, Field

from app.schemas.sche_pet import PetInfoResponse


class VeterinaryClinicRequest(BaseModel):
    name: Optional[str]
    address: Optional[str]
    phone_number: Optional[str]
    email: Optional[str]

class VeterinaryClinicResponse(BaseModel):
    id: int
    name: str
    address: str
    phone_number: str
    email: str

class HealthReportRequest(BaseModel):
    pet_id: Optional[int]
    veterinary_clinic_id: Optional[int]
    weight: Optional[float]
    health_condition: Optional[str]
    description: Optional[str]

class HealthReportResponse(BaseModel):
    id: int
    pet: PetInfoResponse
    veterinary_clinic: VeterinaryClinicResponse
    created_at: date
    weight: float
    health_condition: str
    description: str

class HealthReports(BaseModel):
    health_reports: List[HealthReportResponse]
