#!/usr/bin/python3
"""Defines a square"""


class Square:
    """it represents a square"""
    def __init__(self, size=0):
        """initialize new square.
        Args:
        size(int): Size of new square"""
        self.__size = size

    @property
    def size(self):
        """gets the size of square"""
        return (self.__size)

    @size.setter
    def size(self, value):
        """it sets the value of square"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """returns size of a square"""
        return (self.__size * self.__size)

    def my_print(self):
        """it prints square wit # character"""
        if self.size == 0:
            print("")
        else:
            for i in range(0, self.__size):
                [print("#", end="") for j in range(self.__size)]
                print("")
