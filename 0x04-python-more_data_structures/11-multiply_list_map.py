#!/usr/bin/python3
# 11-multiply_list_map.py


def multiply_list_map(my_list=[], number=0):
    """it returns a list with all the values multiplied by a number"""
    new_list = my_list.copy()
    new_list = list(map(lambda x: x*number, my_list))
    return new_list
