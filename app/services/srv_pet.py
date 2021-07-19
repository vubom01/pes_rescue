from fastapi import Depends, HTTPException
from fastapi.security import HTTPBearer
from pydantic import ValidationError
from starlette import status

from app.core.config import settings
from app.db.base import mysql
from app.schemas.sche_pet import PetInfoRequest


class PetService(object):
    __instance = None

    @staticmethod
    def is_exist_pet(name: str):
        cursor = mysql.cursor()
        query = 'select * from pets where name = %s;'
        cursor.execute(query, (name,))
        pet = cursor.fetchone()
        if not pet:
            return None
        return pet

    @staticmethod
    def pet_input_info(data: PetInfoRequest):
        cursor = mysql.cursor()
        query = 'insert into pets(name, age, color, health_condition, weight, species, description)' \
                'values (%s, %s, %s, %s, %s, %s, %s);'

        cursor.execute(query, (
            data.name, data.age, data.color, data.health_condition, data.weight, data.species, data.description,))
        mysql.commit()
