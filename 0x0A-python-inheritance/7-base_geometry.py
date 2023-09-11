#!/usr/bin/python3
# 7-base_geometry.py
"""it defines a class BaseGeometry"""


class BaseGeometry:
    """it represents BaseGeometry"""
    def area(self):
        """it represent area"""
        raise Exception("area() is not implemented")
    def integer_validator(self, name, value):
        """it validates value"""
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
