#!/usr/bin/python3
"""say_my_name module"""


def say_my_name(first_name, last_name=""):
    """function that prints My name is <first name> <last name>
    Args:
        first_name: the first name (string)
        last_name: the last name (string)
    """
    if type(first_name) != str:
        raise TypeError("first_name must be a string")
    if type(last_name) != str:
        raise TypeError("last_name must be a string")
    print("My name is", first_name, last_name)
