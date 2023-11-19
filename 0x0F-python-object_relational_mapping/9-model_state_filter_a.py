#!/usr/bin/python3
"""
Lists all state object with 'a' from hbtn_06_6_usa database
"""
import sys
from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import (create_engine)

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    for i in session.query(State).filter(State.name.like('%a%')):
        print(i.id, i.name, sep=": ")
