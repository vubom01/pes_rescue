from typing import Optional

from pydantic import BaseModel


class PetInfoRequest(BaseModel):
    name: Optional[str]
    age: Optional[str]
    color: Optional[str]
    health_condition: Optional[str]
    weight: Optional[float]
    description: Optional[str]
    species: Optional[str]

