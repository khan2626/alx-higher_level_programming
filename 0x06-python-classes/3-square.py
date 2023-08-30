#!/usr/bin/python3
"""it defines a square"""


class Square:
    """it represent a square"""
    def __init__(self, size=0):
        """it initializes a new square.
        Args:
        size (int): The size of a new square."""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
    def area(self):
        """Returns area of a square"""
        return (self.__size * self.__size)
