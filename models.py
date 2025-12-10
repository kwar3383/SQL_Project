from sqlalchemy import Column, Integer, String, Table, UniqueConstraint, ForeignKey
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import relationship

# base is an abstract base class - the sql alchemy models will inherit from this class
Base = declarative_base()

# sets up link table with activity_id and person_id as foreign keys
# Base.metadata is a container object that keeps together many features of the database

person_activity = Table('person_activity',
                        Base.metadata,
                        Column('id', Integer, primary_key=True),
                        Column('activity_id', ForeignKey('activity.id')),
                        Column('person_id', ForeignKey('person.id')),
                        UniqueConstraint('activity_id', 'person_id')
                        )


class Location:
    __tablename__ = "location"
    id = Column(Integer, primary_key=True, autoincrement=True)
    room = Column(String, nullable=False)
    activities = relationship("Activity", backref="location")


# sets up an activity table, this references "attendees" via the person_activities table
class Activity(Base):
    __tablename__ = 'activity'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, unique=True, nullable=False)
    attendees = relationship("Person",
                             secondary=person_activity,
                             order_by='(Person.last_name, Person.first_name)',
                             back_populates="activities")
    location_id = Column(Integer, ForeignKey("location_id"), default=None)

    # gives a representation of an activity for printing out
    def __repr__(self):
        return f"<Activity({self.name})>"


# sets up person table, this references activities via the person activities table
class Person(Base):
    __tablename__ = 'person'
    id = Column(Integer, primary_key=True, autoincrement=True)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    activities = relationship("Activity",
                              secondary=person_activity,
                              order_by='Activity.name',
                              back_populates="attendees")

    # gives a representation of a person(for printing out)
    def __repr__(self):
        return f"<Person({self.first_name} {self.last_name})>"

    # include a method
    def greeting(self):
        print(f"{self.first_name} says hello!")
