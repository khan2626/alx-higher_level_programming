#!/usr/bin/python3
# 100-weight_average.py


def weight_average(my_list=[]):
    """returns weighted average of all integers tuple"""
    if not my_list:
        return 0
    else:
        numerator = 0
        denominator = 0
        for tup in my_list:
            numerator += tup[0] * tup[1]
            denominator += tup[1]
        return (numerator/denominator)
