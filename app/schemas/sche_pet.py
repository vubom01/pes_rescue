from typing import List, Optional

from pydantic import BaseModel


class PetItemResponse(BaseModel):
    name: str
    age: str
    color: str
    health_condition: str
    weight: float
    species: str
    url: str
    description: Optional[str]
