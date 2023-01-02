from sqlalchemy import create_engine, ForeignKey, Column, String, Integer, CHAR
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class Person(Base):
    __tablename__ = "people"

    # social security number
    ssn = Column("ssn", Integer, primary_key=True)
    first_name = Column("first_name", String)
    last_name = Column("last_name", String)
    gender = Column("gender", CHAR)

    def __init__(self, ssn, first_name, last_name, gender):
        self.ssn = ssn
        self.first_name = first_name
        self.last_name = last_name
        self.gender = gender

    def __repr__(self):
        return f"({self.ssn}) {self.first_name}"


# create database connection
engine = create_engine("sqlite:///testdb.db", echo=True)

# create all classes into db table like 'Person'
Base.metadata.create_all(bind=engine)