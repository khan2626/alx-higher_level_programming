#!/bin/python3
"""It defines a function that appends to a text file"""


def append_write(filename="", text=""):
    """it appends string to text file"""
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
