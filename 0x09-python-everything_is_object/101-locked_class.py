#!/usr/bin/python3
"""it defines a class LockedClass"""


class LockedClass:
    """it prevent creation of new attribute"""

    __slots__ = ["first_name"]
