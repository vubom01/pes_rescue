from app.db.base import mysql

class UserService(object):
    @staticmethod
    def authentication(username: str, password: str):
        cursor = mysql.cursor()
        query = 'select * from users where username = %s and password = %s'
        cursor.execute(query, (username, password,))
        account = cursor.fetchone()
        return account
