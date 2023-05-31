#!/usr/bin/python3
"""Defiation of class_Square."""


class Square:
    """Represenatation square."""

    def __init__(self, size=0):
        """Initialization a new_square.

        Arguments:
            size (int): size of  new_square.
        """
        self.size = size

    @property
    def size(self):
        """Get/set  current_size of square."""
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Return current_area of square."""
        return (self.__size * self.__size)

    def __eq__(self, other):
        """Defined the == comparision to square."""
        return self.area() == other.area()

    def __ne__(self, other):
        """Defined the != comparison to square."""
        return self.area() != other.area()

    def __lt__(self, other):
        """Defined the < comparison to square."""
        return self.area() < other.area()

    def __le__(self, other):
        """Defined the <= comparison to  square."""
        return self.area() <= other.area()

    def __gt__(self, other):
        """Defined the > comparison to  square."""
        return self.area() > other.area()

    def __ge__(self, other):
        """Defined the >= comparison to Square."""
        return self.area() >= other.area()
