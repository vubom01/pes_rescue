import cloudinary.uploader
import jwt
from fastapi import Depends, HTTPException, UploadFile, File
from fastapi.security import HTTPBearer
from pydantic import ValidationError
from starlette import status

from app.core.config import settings
from app.core.security import get_password_hash, verify_password
from app.db.base import mysql
from app.schemas.sche_token import TokenPayload
from app.schemas.sche_user import UserRegisterRequest, UserUpdateRequest, UserItemResponse


class PetService(object):
    __instance = None

    reusable_oauth2 = HTTPBearer(
        scheme_name='Authorization'
    )

    @staticmethod
    def upload_pet_image(pet_id: int, image: File):
        folder = "pet-rescue/" + str(pet_id)
        result = cloudinary.uploader.upload(image, folder=folder)
        return {
            "url": result.get('url')
        }

    @staticmethod
    def get_list_pets():
        cursor = mysql.cursor()
        query = 'select * from pets'
        cursor.execute(query, )
        pets = cursor.fetchall()
        return pets

    @staticmethod
    def get_pet_by_id(pet_id: int):
        cursor = mysql.cursor()
        query = 'select p.name, p.age, p.color, p.health_condition, p.weight, p.species, p.description, i.url ' \
                'from pets p inner join pet_images i on p.id = i.pet_id where p.id = %s limit 1;'
        cursor.execute(query, pet_id, )
        pet = cursor.fetchone()
        if not pet:
            raise HTTPException(status_code=404, detail="Pet not found")
        return pet
