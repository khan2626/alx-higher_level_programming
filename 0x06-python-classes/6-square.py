#!/usr/bin/python3
"""it defines a square"""


class Square:
    """it represents a square"""
    def __init__(self, size=0, position=(0, 0)):
        """it initialize a new square.
        Args:
        size (int): size of new square.
        position (int, int): position of new square."""
        self.__size = size
        self.__position = position

        @property
        def size(self):
            """it gets the size of square"""
            return (self.__size)

        @size.setter
        def size(self, value):
            """it sets the size of square"""
            if not isinstance(value, int):
                raise TypeError("size must be an integer")
            elif value < 0:
                raise ValueError("size must be >= 0")
            self.__size = value

        @property
        def position(self):
            """it gets the position of square"""
            return (self.__position)

        @position.setter
        def position(self, value):
            """it set the position"""
            if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(num, int) for num in value) or
                not all(num >= 0 for num in value)):
                raise TypeError("position must be a tuple of 2 positive integers")
            self.__position = value
            
        def area(self):
            """returns size of square"""
            return (self.__size * self.__size)

    def my_print(self):
        """prints square with # character"""
        if self.__size == 0:
            print("")
            return
        for i in range(0, self. __position[1]):
            print("")
            for i in range(0, self.__size):
                for j in range(0, self.__position[0]):
                    print(" ", end="")
                    for k in range(0, self.__size):
                        print("#", end="")
                    print("")
