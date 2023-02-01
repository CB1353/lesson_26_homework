import os

from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

db_file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'database.db')

engine = create_engine(f'sqlite:///{db_file_path}')

Base = declarative_base(engine)
Session = sessionmaker(bind=engine)
