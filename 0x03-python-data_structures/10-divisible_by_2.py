#!/usr/bin/python3
# 10-divisible_by_2.py


def divisible_by_2(my_list=[]):
    """finds all multiple of 2 in a list"""
    num = []
    for i in range(len(my_list)):
        if my_list[i] %2 == 0:
            num.append(True)
        else:
            num.append(False)

    return (num)
