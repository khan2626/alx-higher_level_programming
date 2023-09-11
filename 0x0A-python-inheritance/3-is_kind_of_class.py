#!/usr/bin/python3
# 3-is_kind_of_class.py
"""it defines a function is_kind_of_class"""


def is_kind_of_class(obj, a_class):
    """it returns True/False if obj is instance of class"""
    if not isinstance(obj, a_class):
        return False
    return True
