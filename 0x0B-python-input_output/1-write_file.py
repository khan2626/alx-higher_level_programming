#!/usr/bin/python3
"""it defines a funtion that write to atxt file"""


def write_file(filename="", text=""):
    """it writes to a txt file and returns number of char"""
    with open(filename, 'w', encoding="utf-8") as f:
        return f.write(text)
