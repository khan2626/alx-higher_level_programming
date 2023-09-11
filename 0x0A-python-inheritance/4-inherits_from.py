#!/usr/bin/python3
# 4-inherits_from.py
"""it defines a function inherits_from"""


def inherits_from(obj, a_class):
    """it checks if obj is instance of subclass"""
    return issubclass(type(obj), a_class)
