#!/usr/bin/python3
# 8-simple_delete.py


def simple_delete(a_dictionary, key=""):
    """it deletes a key in a dictionary"""
    if a_dictionary.get(key) is not None:
        del a_dictionary[key]
        return a_dictionary
