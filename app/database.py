from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os

username = 'root'
password = ''
host = 'localhost'
port = 3306  # default MySQL port
database_name = 'svc-gym'

DB_URL = DB_URL = os.getenv("DB_URL")
engine = create_engine(f"mysql+pymysql://{username}:{password}@{host}:{port}/{database_name}")
SessionLocal = sessionmaker(autocommit=False,autoflush=False, bind=engine)

Base = declarative_base()