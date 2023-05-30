#!/usr/bin/python3
""" class's name is Square"""


class Square:
    
    def __init__(self, size=0):
        """Initialization a new_square.

        Arguments:
            size (int): a size of the new_square.
        """
        self.size = size

    @property
    def size(self):
         """Get/set the current_size of square."""
         return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Return current_area of the square."""
        return (self.__size * self.__size)
