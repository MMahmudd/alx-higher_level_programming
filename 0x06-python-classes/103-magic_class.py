#!/usr/bin/python3
"""Defination of a MagicClass matching_exactly a bytecode given by alx."""

import math


class MagicClass:
    """Repres a circle."""

    def __init__(self, radius=0):
        """Initialization a MagicClass.

        Arguments:
            radius (float or int):  radius of the new_MagicClass.
        """
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError("radius must be a number")
        self.__radius = radius

    def area(self):
        """Returning the area of MagicClass."""
        return (self.__radius ** 2 * math.pi)

    def circumference(self):
        """Returning circumference of  MagicClass."""
        return (2 * math.pi * self.__radius)
