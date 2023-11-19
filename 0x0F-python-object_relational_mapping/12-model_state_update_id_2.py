#!/usr/bin/python3
"""
Changes name of a state object from database hbtn_0e_6_usa
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
    nw_instance = session.query(State).filter_by(id=2).first()
    nw_instance.name ='New Mexico'
    session.commit()
