from fastapi import APIRouter

from app.api import api_login, api_pet, api_register, api_user, api_working_time

router = APIRouter()

router.include_router(api_login.router, tags=["login"], prefix="/login")
router.include_router(api_register.router, tags=["register"], prefix="/register")
router.include_router(api_user.router, tags=["user"], prefix="/users")
router.include_router(api_pet.router, tags=["pet"], prefix="/pets")
router.include_router(api_working_time.router, tags=["working_time"], prefix="/working_time")