from fastapi import APIRouter

from app.api import api_login

router = APIRouter()

router.include_router(api_login.router, tags=["login"], prefix="/login")
