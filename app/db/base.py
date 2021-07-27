import cloudinary as cloudinary
import pymysql.cursors

from app.core.config import settings

cloudinary.config(
    cloud_name="pet-rescue",
    api_key="653773119299745",
    api_secret="0isRuiudDQPpDWy05rBzno4BqVg"
)
mysql = pymysql.connect(host=settings.MYSQL_HOST,
                        user=settings.MYSQL_USER,
                        password=settings.MYSQL_PASSWORD,
                        db=settings.MYSQL_DB,
                        charset='utf8mb4',
                        cursorclass=pymysql.cursors.DictCursor)
