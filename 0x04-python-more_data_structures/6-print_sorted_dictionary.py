#!/usr/bin/python3
# 6-print_sorted_dictionary.py


def print_sorted_dictionary(a_dictionary):
    """prints a dictionary by ordered keys"""
    new_dict = sorted(a_dictionary.keys())
    for i in new_dict:
        print("{}: {}".format(i, a_dictionary[i]))
