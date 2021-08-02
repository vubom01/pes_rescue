from fastapi import APIRouter, Depends

from app.helpers.login_manager import PermissionRequired
from app.schemas.sche_veterinary_clinic import VeterinarianRequest

router = APIRouter()

@router.post('', dependencies=[Depends(PermissionRequired('admin'))])
def create_veterinarian(req: VeterinarianRequest):
    return {
        'veterinarian_id': 1
    }
