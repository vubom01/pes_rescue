from typing import Optional

from pydantic import BaseModel


class VeterinaryClinicRequest(BaseModel):
    name: Optional[str]
    address: Optional[str]
    phone_number: Optional[str]
    email: Optional[str]

class HealthReportRequest(BaseModel):
    pet_id: Optional[int]
    veterinary_clinic_id: Optional[int]
    weight: Optional[float]
    health_condition: Optional[str]
    description: Optional[str]
