#!/usr/bin/python3
"""creates the State “California” with the City “San Francisco” from
the database hbtn_0e_100_usa"""

from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import Base, State
from relationship_city import City


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
                           argv[1], argv[2], argv[3]), pool_pre_ping=True)

    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    nState = State(name='California')
    nCity = City(name='San Francisco')
    nState.cities.append(nCity)

    session.add(nState)
    session.commit()
