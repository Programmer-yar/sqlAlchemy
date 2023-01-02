from main import Person, session

all_persons = session.query(Person).all()
minnu = session.query(Person).filter(Person.first_name == "Minnu")

for person in minnu:
    print(person.first_name, person.last_name)