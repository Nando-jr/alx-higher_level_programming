#!/usr/bin/python3
"""lookup"""


def lookup(obj):
    """function that returns the list of available
    attributes and methods of an object
    Args:
        obj: an abject
    """
    return dir(obj)
