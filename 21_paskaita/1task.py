from sqlalchemy import Column, create_engine, Integer, String
from sqlalchemy.orm import declarative_base


engine = create_engine('sqlite:///mokykla.db')
Base = declarative_base()

class Mokinys(Base):
    __tablename__ = 'mokiniai'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    surname = Column(String)
    grade = Column(Integer)


class Mokytojas(Base):
    __tablename__ = 'mokytojai'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    surname = Column(String)
    subject = Column(String)


Base.metadata.create_all(engine)
