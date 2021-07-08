from app import mysql
import MySQLdb

class UserService(object):
    @staticmethod
    def authentication(username: str, password: str):
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM accounts WHERE username = %s AND password = %s', (username, password,))
        account = cursor.fetchone()
        return account
