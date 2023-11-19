#!/usr/bin/python3
"""
Prints state object with name passed as argument
"""
import sys
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    i = session.query(State).filter(State.name == (sys.argv[4]))
    try:
        print(i[0].id)
    except IndexError:
        print("Not found")
