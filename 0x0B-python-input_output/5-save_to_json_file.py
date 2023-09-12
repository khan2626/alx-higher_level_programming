#!/usr/bin/python3
"""Defines function that write obt to txt file"""
import json


def save_to_json_file(my_obj, filename):
    """Uses json to write an object to test file"""
    with open(filename, "w",) as f:
        json.dump(my_obj, f)
