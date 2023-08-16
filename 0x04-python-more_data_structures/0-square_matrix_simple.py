#!/usr/bin/python3
# 0-square_matrix_simple.py


def square_matrix_simple(matrix=[]):
    """it computes the square value of all integers of a matix"""
    new_matrix = list(map(lambda x: [x**2 for x in x], matrix))
    return new_matrix
