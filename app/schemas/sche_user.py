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

