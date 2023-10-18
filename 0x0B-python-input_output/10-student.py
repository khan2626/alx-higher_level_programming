#!/usr/bin/python3
"""It defines class student"""


class Student:
    """Represent a student"""
    def __init__(self, first_name, last_name, age):
        """It initializes a new student"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """it gets dictionary representation of student"""
        if (type(attrs) == list and all(type(ele) == str for ele in attrs)):
            return {k: getattr(self, k) for k in attrs if hasattr(self, k)}
        return self.__dict__