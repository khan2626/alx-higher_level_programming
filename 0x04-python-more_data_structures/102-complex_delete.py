#!/usr/bin/python3
# 102-complex_delete.py


def complex_delete(a_dictionary, value):
    """deletes keys with a specific value in a dictionary"""
    key_list = list(a_dictionary.keys())
    for val in key_list:
        if value == a_dictionary.get(val):
            del a_dictionary[val]

    return (a_dictionary)
