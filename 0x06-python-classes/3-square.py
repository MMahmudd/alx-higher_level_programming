#!/usr/bin/python3
""" Square is the name of class."""


class Square:

    def __init__(self, size=0):
        """Initialization a new_square.

        Arguments:
            size (int): size of the new_square.
        """
        if not isinstance(size, int):
            raise TypeError("size should be an integer")
        elif size < 0:
            raise ValueError("size should be >= 0")
        self.__size = size

    def area(self):
        """Return the current_area of  square."""
        return (self.__size * self.__size)
