#!/usr/bin/python3
"""prints all City objects from the database hbtn_0e_14_usa"""

from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
                           argv[1], argv[2], argv[3]))

    Session = sessionmaker(bind=engine)
    session = Session()
    c = session.query(City, State).join(State).all()
    for city, state in c:
        print("{}: ({:d}) {}".format(state.name, city.id, city.name))

    session.commit()
    session.close()
