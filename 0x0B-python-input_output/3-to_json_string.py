#!/usr/bin/python3
"""it defines string to jason function"""
import jason


def to_json_string(my_obj):
    """it returns jason representation of string"""
    return jason.dumps(my_obj)
