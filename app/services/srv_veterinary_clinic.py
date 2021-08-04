from datetime import date

from app.db.base import mysql
from app.schemas.sche_veterinary_clinic import VeterinaryClinicRequest, HealthyReportRequest


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

    @staticmethod
    def update_veterinary_clinic(id: int, data: VeterinaryClinicRequest):
        cursor = mysql.cursor()
        query = 'update veterinary_clinic set name = %s, address = %s, phone_number = %s, email = %s where id = %s'
        cursor.execute(query, (data.name, data.address, data.phone_number, data.email, id))
        mysql.commit()

    @staticmethod
    def get_list_healthy_report(id: int, start_at: date, end_at: date):
        if start_at is None:
            start_at = '1000-01-01'
        if end_at is None:
            end_at = '3000_12_31'
        cursor = mysql.cursor()
        query = 'select pet_id, created_at, veterinary_clinic_id, health_condition, weight, description from  ' \
                ' health_report where veterinary_clinic_id = %s and created_at between %s and %s order by created_at;'
        cursor.execute(query, (id, start_at, end_at,))
        healthy_reports = cursor.fetchall()
        return healthy_reports
