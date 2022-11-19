#!/usr/bin/python3
"""Square Class"""


class Square:
    """class Square that defines a square"""
    def __init__(self, size=0):
        """
            Instantiation with size
        Args:
            size: size of a square
        """
        self.__size = size

    def area(self):
        """Returns the current square area"""
        return (self.__size * self.__size)

    @property
    def size(self):
        """Returns size"""
        return self.__size

    @size.setter
    def size(self, size):
        """Set size"""
        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
