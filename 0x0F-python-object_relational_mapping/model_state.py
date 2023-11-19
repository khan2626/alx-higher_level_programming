#!/usr/bin/python3
"""Contains class definition of state"""
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, MetaData

mymetadata = MetaData()
Base = declarative_base(metadata=mymetadata)

class State(Base):
    """represents class State"""
    __tablename__ = 'states'
    id = Column(Integer, unique=True, nullable=False, primary_key=True)
    name =Column(String(128), nullable=False)
