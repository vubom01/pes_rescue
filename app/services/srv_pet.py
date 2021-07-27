
import cloudinary.uploader
from fastapi import File, HTTPException

from app.db.base import mysql


class PetService(object):

    @staticmethod
    def upload_pet_image(pet_id: int, image: File):
        folder = "pet-rescue/" + str(pet_id)
        result = cloudinary.uploader.upload(image, folder=folder)
        return {
            "url": result.get('url')
        }

    @staticmethod
    def get_pet_by_id(pet_id: int):
        cursor = mysql.cursor()
        query = 'select p.name, p.age, p.color, p.health_condition, p.weight, p.species, i.url, p.description \
                 from pets p inner join pet_images i on p.id = i.pet_id where id = %s'
        cursor.execute(query, pet_id, )
        pet = cursor.fetchone()
        if not pet:
            raise HTTPException(status_code=404, detail="Pet not found")
        return pet

