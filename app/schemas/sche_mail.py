from fastapi import FastAPI, BackgroundTasks, UploadFile, File, Form
from pydantic import BaseModel, EmailStr
from typing import List, Optional


class EmailSchema(BaseModel):
    email: List[EmailStr]


class BodyEmail(BaseModel):
    subject: Optional[str]
    body: str
