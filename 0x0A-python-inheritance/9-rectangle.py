#!/usr/bin/python3
# 9-rectangle.py
"""it defines a class rectangle"""


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

class Rectangle(BaseGeometry):
    """it represent Rectangle"""
    def __init__(self, width, height):
        """it initializes an instance"""
        self.__width = width
        self.__height = height
        self.integer_validator("width", width)
        self.integer_validator("height", height)

    def area(self):
        """it returns area of rectangle"""
        return self.__width * self.__height

    def __str__(self):
        """it represent rextangle as string"""
        return f"[Rectangle] {self.__width}/{self.__height}"

    def __repr__(self):
        """returns string representation of str()"""
        return self.__str__()
