from decouple import config


DB_NAME = config('DB_NAME')
DB_HOST = config('DB_HOST')
DB_PASSWORD = config('DB_PASSWORD')
DB_PORT = config('DB_PORT')
PORT = config('PORT')
HOST = config('HOST')
BASE_PATH = config('BASE_PATH')
EMAIL = config('EMAIL')
EMAIL_PASSWORD = config('EMAIL_PASSWORD')
CRYPT_KEY = config('CRYPT_KEY')
SECRET_KEY = config('SECRET_KEY')
ALGORITHM = config('ALGORITHM')
ACCESS_TOKEN_EXPIRE_MINUTES = config('ACCESS_TOKEN_EXPIRE_MINUTES')

DATABASE_URI = f'postgres+psycopg2://postgres:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}'
