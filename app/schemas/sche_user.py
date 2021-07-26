from typing import Optional, List

from pydantic import BaseModel


class UserItemResponse(BaseModel):
    id: int
    username: str
    first_name: str
    last_name: str
    email: str
    phone_number: str
    role: str

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

class ListUsers(BaseModel):
    users: List[UserItemResponse]

class UpdatePermissionRequest(BaseModel):
    user_id: int
    role: str
