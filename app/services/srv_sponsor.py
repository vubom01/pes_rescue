from app.db.base import mysql
from app.schemas.sche_sponsor import SponsorRequest


class SponsorService(object):
    @staticmethod
    def is_exist_sponsor(phone_number: str):
        cursor = mysql.cursor()
        query = 'select * from sponsors where phone_number = %s'
        cursor.execute(query, (phone_number,))
        sponsor = cursor.fetchone()
        if not sponsor:
            return None
        return sponsor

    @staticmethod
    def create_sponsor(data: SponsorRequest):
        cursor = mysql.cursor()
        query = 'insert into sponsors (first_name, last_name,address, phone_number, email) values (%s, %s, %s, %s, %s)'
        cursor.execute(query, (data.first_name, data.last_name, data.address, data.phone_number, data.email))
        mysql.commit()

    @staticmethod
    def get_list_sponsors():
        cursor = mysql.cursor()
        query = 'select * from sponsors;'
        cursor.execute(query)
        sponsors = cursor.fetchall()
        return sponsors

    @staticmethod
    def get_sponsor_detail(id: int):
        cursor = mysql.cursor()
        query = 'select * from sponsors where id = %s;'
        cursor.execute(query, (id,))
        sponsor = cursor.fetchone()
        return sponsor

    @staticmethod
    def update_info_sponsor(id: int, data: SponsorRequest):
        cursor = mysql.cursor()
        query = 'update sponsors set first_name = %s, last_name = %s, address = %s, phone_number = %s, email = %s \
            where id = %s'
        cursor.execute(query, (data.first_name, data.last_name, data.address, data.phone_number, data.email, id,))
        mysql.commit()

    @staticmethod
    def delete_sponsor(id: int):
        cursor = mysql.cursor()
        query = 'delete from sponsors where id = %s'
        cursor.execute(query, id)
        mysql.commit()

    @staticmethod
    def get_sum_donations(id: int):
        cursor = mysql.cursor()
        query = 'select sum(donations) as sum_donations from donate_detail where sponsor_id = %s'
        cursor.execute(query, (id,))
        sum_donations = cursor.fetchone().get('sum_donations')
        return sum_donations
