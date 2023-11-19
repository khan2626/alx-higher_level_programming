#!/usr/bin/python3
"""
Prints the first State object from hbtn_0e_6_usa database
"""

from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker
import sys


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                          .format(sys.argv[1], sys.argv[2], sys.argv[3]))
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    i = session.query(State).first()
    if i is None:
        print("Nothing")
    else:
        print(i.id, i.name, sep=": ")
