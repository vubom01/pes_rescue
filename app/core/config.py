from pydantic import BaseSettings


class Settings(BaseSettings):
    # MYSQL_HOST = 'pet-rescue.chhw3ihaqbuw.ap-southeast-1.rds.amazonaws.com'
    MYSQL_HOST = 'localhost'
    # MYSQL_USER = 'admin'
    MYSQL_USER = 'root'
    # MYSQL_PASSWORD = 'admin12345'
    MYSQL_PASSWORD = '13102001'
    MYSQL_DB = 'pet_rescue'

    API_PREFIX = ''
    BACKEND_CORS_ORIGINS = ['*']
    ACCESS_TOKEN_EXPIRE_SECONDS: int = 60 * 60 * 24 * 7  # Token expired after 7 days
    SECRET_KEY = '123456'
    SECURITY_ALGORITHM = 'HS256'

    CLOUD_NAME = 'pet-rescue'
    API_KEY = '653773119299745'
    API_SECRET = '0isRuiudDQPpDWy05rBzno4BqVg'

    MAIL_USERNAME = "vuotnh.hrt@gmail.com"
    MAIL_PASSWORD = "zovlyxhjlmahvesp"
    MAIL_FROM = "vuotnh.hrt@gmail.com"
    MAIL_PORT: int = 587
    MAIL_SERVER = "smtp.gmail.com"
    MAIL_TLS = True
    MAIL_SSL = False
    USE_CREDENTIALS = True


settings = Settings()
