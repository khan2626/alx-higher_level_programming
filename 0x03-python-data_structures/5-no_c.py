#!/usr/bin/python3
# 5-no_c.py


def no_c(my_string):
    """return a new string without c and C character"""

    copy = [x for x in my_string if x != 'c' and x != 'C']
    return ("".join(copy))
