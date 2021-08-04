import cloudinary as cloudinary
import pymysql.cursors
import fastapi_mail

from app.core.config import settings

cloudinary.config(
    cloud_name=settings.CLOUD_NAME,
    api_key=settings.API_KEY,
    api_secret=settings.API_SECRET
)

mail_config = fastapi_mail.ConnectionConfig(
    MAIL_USERNAME=settings.MAIL_USERNAME,
    MAIL_PASSWORD=settings.MYSQL_PASSWORD,
    MAIL_FROM=settings.MAIL_FROM,
    MAIL_PORT=settings.MAIL_PORT,
    MAIL_SERVER=settings.MAIL_SERVER,
    MAIL_TLS=settings.MAIL_TLS,
    MAIL_SSL=settings.MAIL_SSL,
    USE_CREDENTIALS=settings.USE_CREDENTIALS
)

mysql = pymysql.connect(host=settings.MYSQL_HOST,
                        user=settings.MYSQL_USER,
                        password=settings.MYSQL_PASSWORD,
                        db=settings.MYSQL_DB,
                        charset='utf8mb4',
                        cursorclass=pymysql.cursors.DictCursor)
