#!/usr/bin/python3
# 11-multiply_list_map.py


def multiply_list_map(my_list=[], number=0):
    """it returns a list with all the values multiplied by a number"""
    return (list(map((lambda i: i * number), my_list)))
