#!/usr/bin/python3
"""It defines function that reurns dict description"""


def class_to_json(obj):
    """Return the dictionary representation of a simple data structure."""
    return obj.__dict__
