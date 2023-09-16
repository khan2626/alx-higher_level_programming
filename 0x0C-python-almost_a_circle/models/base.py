#!/usr/bin/python3
"""It defines a class base model"""


class Base:
    """Base Model"""
    
    __nb_objects = 0
    
    def __init__(self, id=None):
        """it initializes a new Base.
        Args:
        id (int): The id of a new Base.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
