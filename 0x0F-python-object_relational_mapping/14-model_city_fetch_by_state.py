#!/usr/bin/python3
"""Start link class to table in database
"""
import sys
import sqlalchemy
from model_state import Base, State
from model_city import City
from sqlalchemy.orm import sessionmaker
from sqlalchemy import (create_engine)


def Cities_state():
    """ list of of statesof USA """
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()
    citiesa = session.query(State, City).filter(
        State.id == City.state_id)
    for instance, ciudad in citiesa.order_by(City.id):
        print("{}: ({}) {}".format(instance.name, ciudad.id, ciudad.name))
    session.close()


if __name__ == "__main__":
    Cities_state()
