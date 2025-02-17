import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    TESTING = False

    # secret_key
    SECRET_KEY = os.getenv('SECRET_KEY')

    # configuración para Mysql
    MYSQL_HOST = os.getenv('MYSQL_HOST')
    MYSQL_USER = os.getenv('MYSQL_USER')
    MYSQL_PASSWORD = os.getenv('MYSQL_PASSWORD')
    MYSQL_DB = os.getenv('MYSQL_DB')

    # configuración para flask limiter
    REDIS_HOST = os.getenv('REDIS_HOST')
    REDIS_PORT = os.getenv('REDIS_PORT')
    STORAGE_URI = f"redis://{REDIS_HOST}:{REDIS_PORT}"