#!/usr/bin/python3
"""Defines a function that rea text file"""


def read_file(filename=""):
    """it reads a text file(UTF8) and prints to stdout"""
    with open(filename, encoding="utf-8") as file:
        print(file.read(), end="")
