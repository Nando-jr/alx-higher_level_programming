#!/usr/bin/python3
"""class MyList"""


class MyList(list):
    """Mylist Class"""

    def print_sorted(self):
        """prints the list, but sorted"""
        print(sorted(self))
