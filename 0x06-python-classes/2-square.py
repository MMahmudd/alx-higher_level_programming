#!/usr/bin/python3
""" Square the nemae of class."""


class Square:
    def __init__(self, size=0):
        """Initialization new_Square.

        Arguments:
            size (int): size of the new_square.
        """
        if not isinstance(size, int):
            raise TypeError("size should be an integer")
        elif size < 0:
            raise ValueError("size should be  >= 0")
        self.__size = size
