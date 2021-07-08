from pydantic import BaseModel

class Message(BaseModel):
    status: bool
    message: str
