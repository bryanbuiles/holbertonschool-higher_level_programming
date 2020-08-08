#!/usr/bin/python3
"""Start link class to table in database
"""
import sys
from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import (create_engine)


def States_func():
    """ list of of statesof USA """
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()
    states = session.query(State.id, State.name).first()
    if states is not None:
        print((str("{}: {}".format(states.id, states.name))))
    else:
        print("Nothing")
    session.close()


if __name__ == "__main__":
    States_func()
