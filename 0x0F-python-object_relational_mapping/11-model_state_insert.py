#!/usr/bin/python3
"""Start link class to table in database
"""
import sys
from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import (create_engine)
import sqlalchemy


def States_func():
    """ list of of statesof USA """
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()
    ed_user = State(name='Louisiana')
    session.add(ed_user)
    state = session.query(State).filter_by(name="Louisiana").first()
    print(str(state.id))
    session.commit()
    session.close()


if __name__ == "__main__":
    States_func()
