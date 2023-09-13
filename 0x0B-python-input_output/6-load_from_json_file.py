#!/usr/bin/python
"""Defines a jason file reading function"""
import json


def load_from_json_file(filename):
    """It creats object from a json file"""
    with open(filename) as f:
        return json.load(f)
