#!/usr/bin/python3
"""Defines a module that used for  base
            geometry class_BaseGeometry."""


class BaseGeometry:
    """Reprsentation of base_geometry."""

    def area(self):
        """Nothing implemented yet."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validate_ parameter as an_integer.

        Argumnets:
            name (str): is a name of a parameter.
            value (int): is a parameter to be validated.
        Raise:
            TypeError: If a_value isn't an_integer.
            ValueError: If a_value is <= 0.
        """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
