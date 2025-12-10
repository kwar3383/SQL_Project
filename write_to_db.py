from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from models import Person, Activity

# create some instances of person class
people = [Person(first_name="fred", last_name="smith"),
          Person(first_name="betty", last_name="white"),
          Person(first_name="amy", last_name="winehouse")
          ]

chess = Activity(name="Chess")
fives = Activity(name="Fives")
outdoor_ed = Activity(name="Outdoor Ed")

people[0].activities.append(chess)
people[0].activities.append(fives)
people[1].activities.append(outdoor_ed)
people[1].activities.append(fives)

# connect to activities db
engine = create_engine('sqlite:///activities.db', echo=True)

# create session and add ppl

with Session(engine) as sess:
    sess.add_all(people)
    sess.commit()

