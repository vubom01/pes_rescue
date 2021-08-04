import logging

from fastapi import APIRouter, Depends, HTTPException

from app.helpers.login_manager import PermissionRequired
from app.schemas.sche_veterinary_clinic import VeterinaryClinicRequest
from app.services.srv_veterinary_clinic import VeterinaryClinicService

logger = logging.getLogger()
router = APIRouter()