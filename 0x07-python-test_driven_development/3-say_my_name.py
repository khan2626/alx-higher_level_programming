#!/usr/bin/python3
#3-say_my_name.py
"""it define a function that prints name"""


def say_my_name(first_name, last_name=""):
    """it prints first and last name.
    Args:
    first_name: string parameter
    last_name: string parameter
    Raises:
    TypeErrorr if first_name or last_name are not str
    """

    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
