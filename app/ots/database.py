import os

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

dirname = os.path.dirname(os.path.realpath(__file__))

SQLITE_DB = f'sqlite:///{dirname}/ots.db'
SQLALCHEMY_DATABASE_URL = os.getenv('DATABASE_URL', SQLITE_DB)

SQLALCHEMY_DATABASE_URL = SQLALCHEMY_DATABASE_URL.replace('mysql', 'mysql+pymysql')

connect_args = {}
if SQLALCHEMY_DATABASE_URL.startswith('sqlite'):
    connect_args['check_same_thread'] = False

engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args=connect_args)

""" 
connection = engine.connect()
metadata = db.MetaData()
table = db.Table('table_name', metadata, autoload=True, autoload_with=engine)
"""

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
