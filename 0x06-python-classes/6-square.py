#!/usr/bin/python3
"""Square Class"""


class Square:
    """class Square that defines a square"""
    def __init__(self, size=0, position=(0, 0)):
        """
            Instantiation with size
        Args:
            size: size of a square
            position: position of a square
        """
        self.size = size
        self.position = position

    def area(self):
        """Returns the current square area"""
        return (self.__size * self.__size)

    @property
    def size(self):
        """Returns size"""
        return self.__size

    @size.setter
    def size(self, value):
        """Set size"""
        if type(value) != int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Returns position"""
        return self.__position

    @position.setter
    def position(self, value):
        """Set position"""
        if type(value) != tuple or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if not isinstance(value[0], int) or not isinstance(value[1], int):
            raise TypeError("position must be a tuple of 2 positive integers")
        if value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def my_print(self):
        """Prints in stdout the square with the character #"""
        if self.size == 0:
            print()
            return
        for m in range(self.__position[1]):
            print()
        for n in range(self.size):
            print(" " * self.__position[0], end="")
            print("#" * self.size)
