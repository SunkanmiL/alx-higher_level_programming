#!/usr/bin/python3
"""
    This script lists all State objects that contain the letter a from the
    database hbtn_0e_6_usa
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import State

if __name__ == '__main__':
    args = sys.argv
    if len(args) != 4:
        print("Usage: {} username password database_name".format(args[0]))
        exit(1)
    username = args[1]
    password = args[2]
    data = args[3]
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(username, password, data))
    # create custom session object class from database engine
    Session = sessionmaker(bind=engine)
    # create instance of new custom session class
    session = Session()
    states = session.query(State).filter(State.name.contains('a'))\
                    .order_by(State.id)
    if states is not None:
        for state in states:
            print('{}: {}'.format(state.id, state.name))
    else:
        print('Nothing')