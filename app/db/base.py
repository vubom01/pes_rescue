import pymysql.cursors

MYSQL_HOST = '127.0.0.1'
MYSQL_USER = 'root'
MYSQL_PASSWORD = 'root'
MYSQL_DB = 'pet_rescue'

mysql = pymysql.connect(host=MYSQL_HOST,
                        user=MYSQL_USER,
                        password=MYSQL_PASSWORD,
                        db=MYSQL_DB,
                        charset='utf8mb4',
                        cursorclass=pymysql.cursors.DictCursor)
