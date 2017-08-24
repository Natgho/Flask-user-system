# Author: Sezer Yavuzer Bozkir <admin@sezerbozkir.com>
# License: The GNU General Public License v3.0
# Created Date: 24.08.2017
# Version: 0.1
# Website: https://github.com/Natgho/Flask-user-system

from sqlalchemy import create_engine, ForeignKey
from sqlalchemy import Column, Date, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref
import os
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

# OR, the same with increased verbosity:
load_dotenv(dotenv_path)
# engine = create_engine('mysql+pymysql://root:test_password@172.17.0.2/bumin')
engine = create_engine('mysql+pymysql://{username}:{password}@{host}:{port}/{db}'.format(
    username=os.environ.get('MYSQL_USER'),
    password=os.environ.get('MYSQL_PASSWORD'),
    host=os.environ.get('MYSQL_HOST'),
    port=os.environ.get('MYSQL_PORT'),
    db=os.environ.get('MYSQL_DB_NAME')
))
Base = declarative_base()


########################################################################
class User(Base):
    """"""
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
