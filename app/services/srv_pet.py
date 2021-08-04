from datetime import date

import cloudinary.uploader
from fastapi import File

from app.db.base import mysql
from app.schemas.sche_pet import PetInfoRequest


class PetService(object):

    @staticmethod
    def upload_pet_image(pet_id: int, image: File):
        folder = "pet-rescue/" + str(pet_id)
        result = cloudinary.uploader.upload(image, folder=folder)
        url = result.get('url')
        cursor = mysql.cursor()
        query = 'insert into pet_images (pet_id, url) values (%s,%s);'
        cursor.execute(query, (pet_id, url,))
        mysql.commit()
        return {
            'url': url
        }

    @staticmethod
    def delete_image(pet_id: int, url: str):
        cursor = mysql.cursor()
        query = 'delete from pet_images where pet_id = %s and url = %s'
        cursor.execute(query, (pet_id, url,))
        mysql.commit()

    @staticmethod
    def is_exist_pet(name: str):
        cursor = mysql.cursor()
        query = 'select * from pets where name = %s'
        cursor.execute(query, (name,))
        pet = cursor.fetchone()
        if not pet:
            return None
        return pet

    @staticmethod
    def create_pet(data: PetInfoRequest):
        cursor = mysql.cursor()
        query = 'insert into pets (name, age, color, health_condition, weight, description, species)' \
                'values (%s, %s, %s, %s, %s, %s, %s)'
        cursor.execute(query, (data.name, data.age, data.color, data.health_condition, data.weight,
                               data.description, data.species,))
        mysql.commit()

    @staticmethod
    def get_pet_images(pet_id: int):
        cursor = mysql.cursor()
        query = 'select url from pet_images where pet_id = %s'
        cursor.execute(query, (pet_id,))
        images = cursor.fetchall()
        return images

    @staticmethod
    def get_list_pets(species: str, age: str, gender: str):
        if species is None:
            species1 = 'cat'
            species2 = 'dog'
        else:
            species1 = species2 = species

        if age is None:
            age1 = 'young'
            age2 = 'mature'
            age3 = 'old'
        else:
            age1 = age2 = age3 = age

        if gender is None:
            gender1 = 'male'
            gender2 = 'female'
        else:
            gender1 = gender2 = gender

        cursor = mysql.cursor()
        query = 'select * from pets where species in(%s, %s) and age in(%s, %s, %s) and gender in(%s, %s)'
        cursor.execute(query, (species1, species2, age1, age2, age3, gender1, gender2))
        pets = cursor.fetchall()
        return pets

    @staticmethod
    def get_pet_by_id(pet_id: int):
        cursor = mysql.cursor()
        query = 'select * from pets where id = %s'
        cursor.execute(query, (pet_id,))
        pet = cursor.fetchone()
        return pet

    @staticmethod
    def update_pet_info(pet_id: int, data: PetInfoRequest):
        cursor = mysql.cursor()
        query = 'update pets set name = %s, age = %s, color = %s, health_condition = %s, ' \
                'weight = %s, description = %s, species = %s where id = %s'
        cursor.execute(query, (data.name, data.age, data.color, data.health_condition, data.weight,
                               data.description, data.species, pet_id,))
        mysql.commit()

