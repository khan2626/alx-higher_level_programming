#!/usr/bin/python3
# 9-multiply_by_2.py


def multiply_by_2(a_dictionary):
    """it returns a new diction with all values multiplied by 2"""
    new_dict = a_dictionary.copy()
    key_list = list(new_dict.keys())

    for i in key_list:
        new_dict[i] *= 2

    return new_dict
