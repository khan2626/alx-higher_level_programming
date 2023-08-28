#!/usr/bin/python3

import sys


def safe_print_integer_err(value):
    """it prints an integer"""
    try:
        print("{:d}".format(value), end="")
        return (True)
    except (TypeError, ValueError):
        print("Exception: {}".format(sys.exc_info()[1]), file=sys.stderr)
        return (False)
