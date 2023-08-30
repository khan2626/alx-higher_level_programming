#!/usr/bin/python3
"""it defines a class square"""


class Square:
    """it represents a square"""

    def __init__(self, size=0, position=(0, 0)):
        """it initializes a new square"""

        self.__size = size
        self.__position = position


    @property
    def size(self):
        """it gets size of square"""
        return (self.__size)

    @size.setter
    def size(self, value):
        """it sets the size of square"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = valiue

    @property
    def position(self):
        """it gets the position of square"""
        return (self.__position)

    @position.setter
    def position(self, value):
        """it sets the position of square"""
        if (not isinstance(value, tuple) or
            len(value) != 2 or
            not all(isinstance(num, int) for num in value) or
            not all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Return aeea of square"""
        return (self.__size * self.__size)

    def my_print(self):
        """print the square with # character."""
        if self.size == 0:
            print("")
            return

        [print("") for i in range(0, self.position[1])]
        for i in range(0, self.__size):
            [print(" ",end="") for j in range(0, self.__position[0])]
            [print("#", end="") for k in range(0, self.__size)]
            print("")
