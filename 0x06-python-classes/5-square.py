#!/usr/bin/python3
""" class's nam is Square."""


class Square:
    """ square."""

    def __init__(self, size):
        """Initialization a new_square.

        Arguments:
            size (int): size of the new_square.
        """
        self.size = size

    @property
    def size(self):
        """Get/set the current_size """
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Return the current_ area of square."""
        return (self.__size * self.__size)

    def my_print(self):
        """Printing square with the # char."""
        for ii in range(0, self.__size):
            [print("#", end="") for j in range(self.__size)]
            print("")
        if self.__size == 0:
            print("")
