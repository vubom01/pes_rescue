import cloudinary.uploader
from fastapi import File

from app.db.base import mysql


class PetService(object):

    @staticmethod
    def upload_pet_image(pet_id: int, image: File):
        folder = "pet-rescue/" + str(pet_id)
        result = cloudinary.uploader.upload(image, folder=folder)
        cursor = mysql.cursor()
        print(result.get('url'))
        query = 'insert into pet_images (pet_id, url) values (%s,%s);'
        cursor.execute(query, (pet_id, result.get('url'),))
        mysql.commit()


