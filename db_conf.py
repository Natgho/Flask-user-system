# Author: Sezer Yavuzer Bozkir <admin@sezerbozkir.com>
# License: The GNU General Public License v3.0
# Created Date: 24.08.2017
# Version: 0.1
# Website: https://github.com/Natgho/Flask-user-system

from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
import os
from os.path import join, dirname
from dotenv import load_dotenv
from marshmallow import Schema
from werkzeug.security import generate_password_hash

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

# OR, the same with increased verbosity:
load_dotenv(dotenv_path)
# engine = create_engine('mysql+pymysql://root:test_password@172.17.0.2/bumin')
engine = create_engine('mysql+pymysql://{username}:{password}@{host}:{port}/{db}?charset=utf8'.format(
    username=os.environ.get('MYSQL_USER'),
    password=os.environ.get('MYSQL_PASSWORD'),
    host=os.environ.get('MYSQL_HOST'),
    port=os.environ.get('MYSQL_PORT'),
    db=os.environ.get('MYSQL_DB_NAME')
))
Base = declarative_base()


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    username = Column(String(length=200), unique=True)
    password = Column(String(length=200))
    email = Column(String(length=50))
    country = Column(String(length=100))

    # ----------------------------------------------------------------------
    def __init__(self, username, password, email, country):
        """"""
        self.username = username
        self.password = password
        self.email = email
        self.country = country


class Country(Base):
    __tablename__ = 'countries'

    id = Column(Integer, primary_key=True)
    country_name = Column(String(length=100), unique=True)

    def __init__(self, country_name):
        self.country_name = country_name


# create tables
# TODO Log system will be developed
try:
    Base.metadata.create_all(engine)
except Exception as e:
    print('Database not created', e)


class CountrySerializer(Schema):
    class Meta:
        fields = ('country_name',)


# TODO create add country page
def create_dummy_countries():
    from sqlalchemy.orm import sessionmaker

    Session = sessionmaker(bind=engine)
    session = Session()
    tmp_countries = ["Türkiye", "Almanya", "Fransa", "Ingiltere", "Kazakistan", "Rusya", "Arabistan"]
    for country in tmp_countries:
        session.add(Country(country))
    session.commit()


def create_dummy_users():
    from sqlalchemy.orm import sessionmaker

    dummy_user_session = sessionmaker(bind=engine)
    session = dummy_user_session()
    tmp_users = [
        {
            'username': "Sezer",
            'password': "test123",
            "email": "sezer@sezer.com",
            "country": "Türkiye"
        },
        {
            'username': "Barış",
            'password': "123test!.",
            "email": "baris@baris.com",
            "country": "Almanya"
        },
        {
            'username': "BengiSu",
            'password': "123test123",
            "email": "bengisu@bengisu.com",
            "country": "Ingiltere"
        },
        {
            'username': "Ayça",
            'password': "123test123",
            "email": "ayca@ayca.com",
            "country": "Rusya"
        }

    ]
    for user in tmp_users:
        session.add(User(user['username'],
                         generate_password_hash(user['password']),
                         user['email'],
                         user['country']))
    session.commit()
