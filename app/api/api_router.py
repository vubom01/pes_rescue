from fastapi import APIRouter

from app.api import (api_login, api_pet, api_register, api_user,
                     api_work_schedule, api_veterinary_clinic, api_sponsor)

router = APIRouter()

router.include_router(api_login.router, tags=["login"], prefix="/login")
router.include_router(api_register.router, tags=["register"], prefix="/register")
router.include_router(api_user.router, tags=["user"], prefix="/users")
router.include_router(api_pet.router, tags=["pet"], prefix="/pets")
router.include_router(api_work_schedule.router, tags=["work_schedule"], prefix="/work_schedule")
router.include_router(api_veterinary_clinic.router, tags=["veterinary_clinic"], prefix="/veterinary_clinic")
router.include_router(api_sponsor.router, tags=["sponsor"], prefix="/sponsors")
