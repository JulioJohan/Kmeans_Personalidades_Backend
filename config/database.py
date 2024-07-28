from sqlalchemy import create_engine, MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import URL



SQLALCHEMY_DATABASE_URL = 'mysql+mysqlconnector://root:USwtNhFAGtvYQggRXNOWuXkRrPRxbKeT@roundhouse.proxy.rlwy.net:59831/railway'

# UrlBD Mysql
engine = create_engine(
    SQLALCHEMY_DATABASE_URL
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
