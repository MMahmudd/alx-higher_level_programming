#!/usr/bin/python3
"""Defines a class named Rectangle."""


class Rectangle:
    """Represents Rectangle."""

    def __init__(self, width=0, height=0):
        """Initialization a new_Rectangle.

        Argumnets:
            width (int): Width of new_rectangle.
            height (int): Height of new_rectangle.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Getter/setter width of Rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Getter/setter height of Rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Returns an area of Rectangle."""
        return (self.__width * self.__height)

    def perimeter(self):
        """Returns a perimeter of Rectangle."""
        if self.__width == 0 or self.__height == 0:
            return (0)
        return ((self.__width * 2) + (self.__height * 2))