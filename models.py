from sqlalchemy import ForeignKey, Column, String, Integer, CHAR
from sqlalchemy.ext.declarative import declarative_base

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


class Thing(Base):
    __tablename__ = "things"

    tid = Column("tid", Integer, primary_key=True)
    description = Column("description", String)
    owner = Column(Integer, ForeignKey("people.ssn"))

    def __init__(self, tid, description, owner):
        self.tid = tid
        self.description = description
        self.owner = owner

    def __repr__(self):
        return self.tid

