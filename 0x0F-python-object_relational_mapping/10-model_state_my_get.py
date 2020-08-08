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

    if session.query(State).filter(State.name == '{}'
                                   .format(sys.argv[4])).first():
        for id, state_name in session.query(State.id, State.name)\
                .filter(State.name == '{}'
                        .format(sys.argv[4])).order_by(State.id):
            print("{}".format(id))
    else:
        print("Not found")

    session.close()


if __name__ == "__main__":
    States_func()
