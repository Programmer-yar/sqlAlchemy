from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Person, Thing, Base

# create database connection
engine = create_engine("sqlite:///testdb.db", echo=True)

# create all classes into db table like 'Person'
Base.metadata.create_all(bind=engine)

# class
Session = sessionmaker(bind=engine)
# instance
session = Session()

# person = Person(12387, "john", "Doe", "m")
# session.add(person)
# session.commit()

# p1 = Person(67123, "Minnu", "Chinnu", "m")
# session.add(p1)
# session.commit()

# p1 = session.query(Person).filter(Person.ssn == 67123).one()

# t1 = Thing(1, "Car", p1.ssn)
# session.add(t1)
# session.commit()

# all_persons = session.query(Person).all()
# minnu = session.query(Person).filter(Person.first_name == "Minnu")

# for person in minnu:
#     print(person.first_name, person.last_name)

all_things = session.query(Thing).all()

for thing in all_things:
    print(thing.description)