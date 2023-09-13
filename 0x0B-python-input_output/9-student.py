#!/usr/bin/python3
"""It defines a class student"""


class Student:
    """it represents a student"""
    def __init__(self, first_name, last_name, age):
        """It initializes a new student"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Get a dictionary representation of student"""
        return self.__dict__
