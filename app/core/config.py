from pydantic import BaseSettings


class Settings(BaseSettings):
    MYSQL_HOST = 'us-cdbr-east-04.cleardb.com'
    MYSQL_USER = 'bb77b7bc8d9d31'
    MYSQL_PASSWORD = '23e164c8'
    MYSQL_DB = 'heroku_b6f0bc9b22feae3'
    API_PREFIX = ''
    BACKEND_CORS_ORIGINS = ['*']
    ACCESS_TOKEN_EXPIRE_SECONDS: int = 60 * 60 * 24 * 7  # Token expired after 7 days
    SECRET_KEY = '123456'
    SECURITY_ALGORITHM = 'HS256'


settings = Settings()
