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


settings = Settings()
