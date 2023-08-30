#!/usr/bin/python3
"""it defines a square"""

class Square:
    """it represents a square"""
    def __init__(self, size=0):
        """initializes a new square."""
        self.__size = size

    @property
    def size(self):
        """gets current size of square"""
        return (self.__size)

    @size.setter
    def size(self, value):
        """Sets the size of the square"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
    
    def area(self):
        """Returns area of square"""
        return (self.__size * self.__size)
