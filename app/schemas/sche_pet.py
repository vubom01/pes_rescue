from typing import Optional

from pydantic import BaseModel


class PetInfoRequest(BaseModel):
    name: str
    age: str
    color: str
    health_condition: str
    weight: float
    species: str
    description: Optional[str]
