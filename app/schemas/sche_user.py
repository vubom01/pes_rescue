from typing import List, Optional

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

class ListUsers(BaseModel):
    users: List[UserItemResponse]

class Role(BaseModel):
    user_id: int
    role: str

class PasswordUpdate(BaseModel):
    current_password: str
    update_password: str

class UserPassword(BaseModel):
    id: int
    password: str
