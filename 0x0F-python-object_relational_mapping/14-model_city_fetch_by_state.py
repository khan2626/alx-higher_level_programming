#!/usr/bin/python3
"""
Prints state object with the name passed as argument
"""
import sys
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker
from model_city import City

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    for i in (session.query(State.name, City.id, City.name)
                     .filter(State.id == City.state_id)):
        print(i[0] + ": (" + str(i[1]) + ") " + i[2])
