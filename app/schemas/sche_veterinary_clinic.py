from typing import Optional

from pydantic import BaseModel


class VeterinaryClinicRequest(BaseModel):
    name: Optional[str]
    address: Optional[str]
    phone_number: Optional[str]
    email: Optional[str]
