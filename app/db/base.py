import pymysql.cursors
from app.core.config import settings

mysql = pymysql.connect(host=settings.MYSQL_HOST,
                        user=settings.MYSQL_USER,
                        password=settings.MYSQL_PASSWORD,
                        db=settings.MYSQL_DB,
                        charset='utf8mb4',
                        cursorclass=pymysql.cursors.DictCursor)
