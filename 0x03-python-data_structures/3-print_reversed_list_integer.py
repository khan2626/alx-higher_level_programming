#!/usr/bin/python3
# 3-print_reversed_list_integer.py


def print_reversed_list_integer(my_list=[]):
    """print in reverse all integer list"""

    my_list.reverse()
    for i in my_list:
        print("{:d}".format(i))
