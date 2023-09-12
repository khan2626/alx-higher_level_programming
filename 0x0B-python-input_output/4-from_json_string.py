#!/usr/bin/python3
"""it defines function that write obj to txt using json"""
import json


def from_json_string(my_str):
    """It writes object to text file"""
    return json.loads(my_str)
