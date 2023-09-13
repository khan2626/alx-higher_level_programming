#!/usr/bin/python3
"""It defines a class student"""


class Student:
    """it represents a student"""
    def __init__(self, first_name, last_name, age):
        """it initializes a new student"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Gets dictionary representation of student"""
        if (type(attrs) == list and all(type(ele) == str for ele in attrs)):
            return {k: getattr(self, k) for k in attrs if hasattr(self, k)}
        return self.__dict__

    def reload_from_json(self, json):
        """Replace all attributes of the student"""
        for k, v in json.items():
            setattr(self, k, v)
