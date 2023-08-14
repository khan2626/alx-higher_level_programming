#!/usr/bin/python3
# 9-max_integer.py


def max_integer(my_list=[]):
    for num in my_list:
        if my_list == 0:
            return (None)
        else:
            nw_list = sorted(my_list)
            return (nw_list[-1])
