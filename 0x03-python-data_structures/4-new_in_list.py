#!/usr/bin/python3
# 4-new_in_list.py


def new_in_list(my_list, idx, element):
    """it replaces an element in list without modifying the original list"""

    new_list = my_list.copy()
    for i in new_list:
        if idx < 0 or idx > len(my_list):
            return (new_list)
        else:
            new_list[idx] = element
            return (new_list)
