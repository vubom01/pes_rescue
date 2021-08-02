from typing import Optional

from pydantic import BaseModel


class VeterinarianRequest(BaseModel):
    first_name: Optional[str]
    last_name: Optional[str]
    address: Optional[str]
    phone_number: Optional[str]
    email: Optional[float]
