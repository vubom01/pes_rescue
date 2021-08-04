from fastapi import APIRouter

from app.api import (api_donate_detail, api_health_report, api_login, api_mail,
                     api_pet, api_register, api_sponsor, api_user,
                     api_veterinary_clinic, api_work_schedule)

router = APIRouter()

router.include_router(api_login.router, tags=["login"], prefix="/login")
router.include_router(api_register.router, tags=["register"], prefix="/register")
router.include_router(api_user.router, tags=["user"], prefix="/users")
router.include_router(api_work_schedule.router, tags=["work_schedule"], prefix="/work_schedule")
router.include_router(api_pet.router, tags=["pet"], prefix="/pets")
router.include_router(api_veterinary_clinic.router, tags=["veterinary_clinic"], prefix="/veterinary_clinic")
router.include_router(api_health_report.router, tags=["health_report"], prefix="/health_report")
router.include_router(api_sponsor.router, tags=["sponsor"], prefix="/sponsors")
router.include_router(api_donate_detail.router, tags=["donate_detail"], prefix="/donate_detail")
router.include_router(api_mail.router, tags=["email"], prefix="/email")

