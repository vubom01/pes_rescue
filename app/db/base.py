import cloudinary as cloudinary
import pymysql.cursors
import fastapi_mail

from app.core.config import settings

cloudinary.config(
    cloud_name="pet-rescue",
    api_key="653773119299745",
    api_secret="0isRuiudDQPpDWy05rBzno4BqVg"
)

mail_config = fastapi_mail.ConnectionConfig(
    MAIL_USERNAME="vuotnh.hrt@gmail.com",
    MAIL_PASSWORD="zovlyxhjlmahvesp",
    MAIL_FROM="vuotnh.hrt@gmail.com",
    MAIL_PORT=587,
    MAIL_SERVER="smtp.gmail.com",
    MAIL_TLS=True,
    MAIL_SSL=False,
    USE_CREDENTIALS=True
)
mysql = pymysql.connect(host=settings.MYSQL_HOST,
                        user=settings.MYSQL_USER,
                        password=settings.MYSQL_PASSWORD,
                        db=settings.MYSQL_DB,
                        charset='utf8mb4',
                        cursorclass=pymysql.cursors.DictCursor)
