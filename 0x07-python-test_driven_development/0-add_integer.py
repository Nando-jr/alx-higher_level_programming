#!/usr/bin/python3a
"""add_integer module"""


def add_integer(a, b=98):
    """function that adds 2 integers
    Args:
        a: first number
        b: second number
    Return:
          The sum of the two numbers
    """
    if type(a) != int and type(a) != float:
        raise TypeError("a must be an integer")
    if type(b) != int and type(b) != float:
        raise TypeError("b must be an integer")
    if type(a) == float:
        a = int(a)
    if type(b) == float:
        b = int(b)
    return (a + b)
