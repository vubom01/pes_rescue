import json
import os
from datetime import date
import csv

import cloudinary

from app.db.base import mysql
from app.schemas.sche_sponsor import DonateDetailRequest, SponsorRequest


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
        query = 'select * from sponsors where id = %s'
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
    def create_donate_detail(data: DonateDetailRequest):
        cursor = mysql.cursor()
        query = 'insert into donate_detail (sponsor_id, created_at, update_at, ' \
                'account_number, transaction_code, donations) values (%s, %s, %s, %s, %s, %s)'
        cursor.execute(query, (data.sponsor_id, date.today(), date.today(),
                               data.account_number, data.transaction_code, data.donations))
        mysql.commit()

    @staticmethod
    def update_donate_detail(data: DonateDetailRequest):
        cursor = mysql.cursor()
        query = 'update donate_detail set sponsor_id = %s, update_at = %s, account_number = %s, ' \
                'transaction_code = %s, donations = %s where id = %s'
        cursor.execute(query, (data.sponsor_id, date.today(), data.account_number, data.transaction_code,
                               data.donations, data.id))
        mysql.commit()

    @staticmethod
    def get_donate_detail_by_id(id: int):
        cursor = mysql.cursor()
        query = 'select * from donate_detail where id = %s'
        cursor.execute(query, id)
        donate_detail = cursor.fetchone()
        return donate_detail

    @staticmethod
    def get_list_donate_detail(start_at: date, end_at: date):
        if start_at is None:
            start_at = '1000-01-01'
        if end_at is None:
            end_at = '3000_12_31'

        cursor = mysql.cursor()
        query = 'select dd.id, dd.created_at, dd.sponsor_id, (concat(s.first_name, " ", s.last_name)) as full_name, ' \
                's.email, s.phone_number, dd.account_number, dd.transaction_code, dd.donations ' \
                'from donate_detail dd inner join sponsors s on dd.sponsor_id = s.id ' \
                'where dd.created_at between %s and %s order by created_at'
        cursor.execute(query, (start_at, end_at))
        donate_details = cursor.fetchall()

        fields = ['id', 'created_at', 'sponsor_id', 'full_name', 'email', 'phone_number', 'account_number',
                  'transaction_code', 'donations']
        file_path = os.getcwd() + '\\report\\' + 'donate_detail.csv'
        file = open(file_path, "w", newline="\n")
        writer = csv.writer(file, delimiter=",")

        writer.writerow(fields)
        for field in donate_details:
            writer.writerow(field.values())
        file.close()

        f = open(file_path, "r")
        folder = "donate_detail/" + str(start_at.year) + "/" + str(start_at.month)
        name = "donate_detail_T" + str(start_at.month)
        result = cloudinary.uploader.upload(os.path.basename(f.name), folder=folder, public_id=name,
                                            resource_type='raw')
        url = result.get('url')
        return {
            'url': url
        }


