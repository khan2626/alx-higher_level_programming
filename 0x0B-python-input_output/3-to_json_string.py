#!/usr/bin/python3
"""it defines string to jason function"""
import json


def to_json_string(my_obj):
    """it returns jason representation of string"""
    return json.dumps(my_obj)
