#!/usr/bin/python3
"""class MyInt"""


class MyInt(int):
    """class MyInt that inherits from int"""
    def __init__(self, value):
        self.n = value

    def __eq__(self, other):
        return self.n != other

    def __ne__(self, other):
        return self.n == other
