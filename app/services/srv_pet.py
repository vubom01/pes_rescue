import cloudinary.uploader
from fastapi import File

from app.db.base import mysql


class PetService(object):

    @staticmethod
    def upload_pet_image(pet_id: int, image: File):
        folder = "pet-rescue/" + str(pet_id)
        result = cloudinary.uploader.upload(image, folder=folder)
        cursor = mysql.cursor()
        query = 'insert into pet_images (pet_id, url) values (%s,%s);'
        cursor.execute(query, (pet_id, result.get('url'),))
        mysql.commit()

    @staticmethod
    def get_pet_images(pet_id: int):
        cursor = mysql.cursor()
        query = 'select url from pet_images where pet_id = %s'
        cursor.execute(query, (pet_id,))
        images = cursor.fetchall()
        return images

    @staticmethod
    def get_list_pets():
        cursor = mysql.cursor()
        query = 'select * from pets'
        cursor.execute(query,)
        pets = cursor.fetchall()
        return pets


