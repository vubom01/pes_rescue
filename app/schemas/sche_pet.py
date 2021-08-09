from typing import List, Optional

from pydantic import BaseModel


class PetInfoRequest(BaseModel):
    name: Optional[str]
    age: Optional[str]
    color: Optional[str]
    health_condition: Optional[str]
    weight: Optional[float]
    description: Optional[str]
    species: Optional[str]
    gender: Optional[str]

class Urls(BaseModel):
    urls: List[str]

class PetInfoResponse(BaseModel):
    id: int
    name: str
    age: str
    gender: str
    color: str
    health_condition: str
    weight: float
    description: str
    species: str

    class Url(BaseModel):
        url: str
    images: List[Url]


