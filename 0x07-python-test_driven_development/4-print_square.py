#!/usr/bin/python3
#4-print_square.py
"""it defines a function that print square"""


def print_square(size):
    """it prints square with # character.
    Args:
    size: the size of the square
    Raises:
    TypeError if size is not an int.
    ValueError if size < 0
    TypeError if size is a float and < 0
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")

    for n in range(size):
        [print("#", end="") for m in range(size)]
        print("")
