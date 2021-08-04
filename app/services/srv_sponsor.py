from datetime import date

from app.db.base import mysql
from app.schemas.sche_sponsor import SponsorRequest, DonateDetailRequest


class SponsorService(object):
    @staticmethod
    def get_sponsor(id: int):
        cursor = mysql.cursor()
        query = 'select * from sponsors where id = %s'
        cursor.execute(query, id)
        sponsor = cursor.fetchone()
        return sponsor

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
        query = 'insert into sponsors (first_name, last_name, address, phone_number, email) values (%s, %s, %s, %s, %s)'
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

    @staticmethod
    def is_exist_donate_detail(transaction_code: str):
        cursor = mysql.cursor()
        query = 'select * from donate_detail where transaction_code = %s'
        cursor.execute(query, transaction_code)
        donate_detail = cursor.fetchone()
        return donate_detail

    @staticmethod
    def get_list_donate_detail(start_at: date, end_at: date):
        if start_at is None:
            start_at = '1000-01-01'
        if end_at is None:
            end_at = '3000_12_31'

        cursor = mysql.cursor()
        query = 'select * from donate_detail where created_at between %s and %s'
        cursor.execute(query, (start_at, end_at))
        donate_details = cursor.fetchall()
        return donate_details

    @staticmethod
    def get_donate_detail_by_id(id: int):
        cursor = mysql.cursor()
        query = 'select * from donate_detail where id = %s'
        cursor.execute(query, id)
        donate_detail = cursor.fetchone()
        return donate_detail

    @staticmethod
    def delete_donate_detail(id: int):
        cursor = mysql.cursor()
        query = 'delete from donate_detail where id = %s'
        cursor.execute(query, id)
        mysql.commit()

    @staticmethod
    def get_list_donate_details_of_sponsor(sponsor_id: int, start_at: date, end_at: date):
        if start_at is None:
            start_at = '1000-01-01'
        if end_at is None:
            end_at = '3000_12_31'

        cursor = mysql.cursor()
        query = 'select * from donate_detail where sponsor_id = %s and created_at between %s and %s'
        cursor.execute(query, (sponsor_id, start_at, end_at))
        donate_details = cursor.fetchall()
        return donate_details

    @staticmethod
    def get_total_donations(sponsor_id: int, start_at: date, end_at: date):
        if start_at is None:
            start_at = '1000-01-01'
        if end_at is None:
            end_at = '3000_12_31'

        cursor = mysql.cursor()
        query = 'select sum(donations) as total_donations from donate_detail ' \
                'where sponsor_id = %s and created_at between %s and %s'
        cursor.execute(query, (sponsor_id, start_at, end_at))
        total_donations = cursor.fetchone()
        return total_donations

    @staticmethod
    def create_donate_detail(sponsor_id: int, data: DonateDetailRequest):
        cursor = mysql.cursor()
        query = 'insert into donate_detail (sponsor_id, created_at, account_number, transaction_code, donations) ' \
                'values (%s, %s, %s, %s, %s)'
        cursor.execute(query, (sponsor_id, date.today(), data.account_number, data.transaction_code, data.donations))
        mysql.commit()

    @staticmethod
    def update_donate_detail(id: int, data: DonateDetailRequest):
        cursor = mysql.cursor()
        query = 'update donate_detail set created_at = %s, account_number = %s, transaction_code = %s, donations = %s ' \
                'where id = %s'
        cursor.execute(query, (date.today(), data.account_number, data.transaction_code, data.donations, id))
        mysql.commit()
