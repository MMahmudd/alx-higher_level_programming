#!/usr/bin/python3
"""Defines a class Rmed ReBctangle that's
            inherited from BaseGeometry."""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """implementation of class rectangle
             that is used BaseGeometry."""

    def __init__(self, width, height):
        """Intialization of a new Rectangle.

        Argumnets:
            width (int): is size of the new_Rectangle.
            height (int): is size of the new_Rectangle.
        """
        super().integer_validator("width", width)
        self.__width = width
        super().integer_validator("height", height)
        self.__height = height

    def area(self):
        """Returning an area of class rectangle."""
        return self.__width * self.__height

    def __str__(self):
        """Returning the print() and str()
        hat is represented of a Rectangle."""
        string = "[" + str(self.__class__.__name__) + "] "
        string += str(self.__width) + "/" + str(self.__height)
        return string
