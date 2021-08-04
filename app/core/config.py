from pydantic import BaseSettings


class Settings(BaseSettings):
    MYSQL_HOST = 'sql6.freemysqlhosting.net'
    MYSQL_USER = 'sql6428642'
    MYSQL_PASSWORD = 'SAwqck96ft'
    MYSQL_DB = 'sql6428642'

    API_PREFIX = ''
    BACKEND_CORS_ORIGINS = ['*']
    ACCESS_TOKEN_EXPIRE_SECONDS: int = 60 * 60 * 24 * 7  # Token expired after 7 days
    SECRET_KEY = '123456'
    SECURITY_ALGORITHM = 'HS256'

    CLOUD_NAME = 'pet-rescue'
    API_KEY = '653773119299745'
    API_SECRET = '0isRuiudDQPpDWy05rBzno4BqVg'

    MAIL_USERNAME = 'vuotnh.hrt@gmail.com'
    MAIL_PASSWORD = 'zovlyxhjlmahvesp'
    MAIL_FROM = 'vuotnh.hrt@gmail.com'
    MAIL_PORT = 587,
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_TLS = True
    MAIL_SSL = False
    USE_CREDENTIALS = True


settings = Settings()
