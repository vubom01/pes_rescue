from app.db.base import mysql
from app.schemas.sche_sponsor import SponsorRequest


class SponsorService(object):
    @staticmethod
    def is_exist_sponsor(email: str, phone_number: str):
        cursor = mysql.cursor()
        query = 'select * from sponsors where email = %s and phone_number = %s'
        cursor.execute(query, (email, phone_number))
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
        query = 'select s.id, s.first_name, s.last_name, s.email, ' \
                's.phone_number, s.address, if(sum(d.donations) is null, 0, sum(d.donations))' \
                'as total_donations from sponsors s inner join donate_detail d on s.id = d.sponsor_id where s.id = %s;'
        cursor.execute(query, id)
        sponsor = cursor.fetchone()
        return sponsor

    @staticmethod
    def update_info_sponsor(id: int, data: SponsorRequest):
        cursor = mysql.cursor()
        query = 'update sponsors set first_name = %s, last_name = %s, address = %s, phone_number = %s, email = %s ' \
                'where id = %s'
        cursor.execute(query, (data.first_name, data.last_name, data.address, data.phone_number, data.email, id))
        mysql.commit()

    @staticmethod
    def delete_sponsor(id: int):
        cursor = mysql.cursor()
        query = 'delete from sponsors where id = %s'
        cursor.execute(query, id)
        mysql.commit()


