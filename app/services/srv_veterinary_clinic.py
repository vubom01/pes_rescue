from app.db.base import mysql
from app.schemas.sche_veterinary_clinic import VeterinaryClinicRequest


class VeterinaryClinicService(object):

    @staticmethod
    def is_exist_clinic(name: str):
        cursor = mysql.cursor()
        query = 'select * from veterinary_clinic where name = %s'
        cursor.execute(query, (name,))
        clinic = cursor.fetchone()
        if not clinic:
            return None
        return clinic

    @staticmethod
    def create_clinic(data: VeterinaryClinicRequest):
        cursor = mysql.cursor()
        query = 'insert into veterinary_clinic (name, address, phone_number, email) values (%s, %s, %s, %s)'
        cursor.execute(query, (data.name, data.address, data.phone_number, data.email))
        mysql.commit()

    @staticmethod
    def get_list_veterinary_clinics():
        cursor = mysql.cursor()
        query = 'select * from veterinary_clinic'
        cursor.execute(query)
        clinics = cursor.fetchall()
        return clinics

    @staticmethod
    def get_veterinary_clinic_detail(id: int):
        cursor = mysql.cursor()
        query = 'select * from veterinary_clinic where id = %s'
        cursor.execute(query, id)
        clinic = cursor.fetchone()
        return clinic

    @staticmethod
    def delete_veterinary_clinic(id: int):
        cursor = mysql.cursor()
        query = 'delete from veterinary_clinic where id = %s'
        cursor.execute(query, id)
        mysql.commit()
