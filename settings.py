import os

from dotenv import load_dotenv

load_dotenv()


class Config(object):
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URI')
    SECRET_KEY = os.getenv('SECRET_KEY')


FILE_NAME_CSV = 'opinions.csv'
FLASK_DEBUG = os.getenv('FLASK_DEBUG')
