#!/usr/bin/python3


def safe_print_division(a, b):
    """it divides 2 integers and prints the result."""
    try:
        quotient = a / b
    except (TypeError, ZeroDivisionError):
        quotient = None
    finally:
        print("Inside result: {}".format(quotient))
    return (quotient)
