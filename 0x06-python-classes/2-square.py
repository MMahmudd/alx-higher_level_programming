#!/usr/bin/python3
"""Defination of class sqr."""


class Square:
    """Represent_square."""

    def __init__(self, size=0):
        """Initialize a new_Square.

        Arguments:
            size (int): size of the new_square.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
