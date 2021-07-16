from typing import Optional

from pydantic import BaseModel


class UserItemResponse(BaseModel):
    id: int
    username: str
    first_name: str
    last_name: str
    email: str
    phone_number: str

class UserRegisterRequest(BaseModel):
    username: str
    password: str
    first_name: str
    last_name: str
    email: str
    phone_number: str

class UserUpdateRequest(BaseModel):
    first_name: Optional[str]
    last_name: Optional[str]
    email: Optional[str]
    phone_number: Optional[str]
    password: Optional[str]
