#!/usr/bin/python3
"""MagicClass Class"""

import math


class MagicClass:
    """class that does exactly the same as the following Python bytecode"""
    def __init__(self, radius=0):
        """Instantiation with radius
        Args:
            radius: radius of the magicclass
        """
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError("radius must be a number")
        self.__radius = radius

    def area(self):
        """Returns the area"""
        return (self.__radius ** 2 * math.pi)

    def circumference(self):
        """Return The circumference"""
        return (2 * math.pi * self.__radius)
