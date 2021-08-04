from datetime import date

from app.db.base import mysql
from app.schemas.sche_veterinary_clinic import VeterinaryClinicRequest, HealthReportRequest


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
    def create_health_report(data: HealthReportRequest):
        cursor = mysql.cursor()
        query = 'insert into health_report(pet_id, veterinary_clinic_id, created_at, update_at, weight,' \
                'health_condition, description) values (%s, %s, %s, %s, %s, %s, %s)'
        cursor.execute(query, (data.pet_id, data.veterinary_clinic_id, date.today(), date.today(), data.weight,
                               data.health_condition, data.description))
        mysql.commit()

    @staticmethod
    def get_list_health_reports(start_at: date, end_at: date):
        if start_at is None:
            start_at = '1000-01-01'
        if end_at is None:
            end_at = '3000_12_31'

        cursor = mysql.cursor()
        query = 'select * from health_report where created_at between %s and %s'
        cursor.execute(query, (start_at, end_at))
        health_reports = cursor.fetchall()
        return health_reports

    @staticmethod
    def get_health_report_detail(id: int):
        cursor = mysql.cursor()
        query = 'select * from health_report where id = %s'
        cursor.execute(query, id)
        health_report = cursor.fetchone()
        return health_report
