#!/usr/bin/python3
"""it defines a square"""


class Square:
    """it represents a squqre"""
    def __init__(self, size=0):
        """it initializes a new square"""
        if not isinstance(size, int):
            raise TypeError("ize must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
