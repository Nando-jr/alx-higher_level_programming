#!/usr/bin/python3
"""Rectangle Class"""


BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """class Rectangle that inherits from BaseGeometry
       Attributes:
                  width: width of rectangle
                  height: height of rectangle
    """
    def __init__(self, width, height):
        """Instantiation with width and height"""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
