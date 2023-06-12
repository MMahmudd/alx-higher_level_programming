#!/usr/bin/python3
"""Defines of a class Rectangle, sub_class is Square."""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """implementation of a class square."""

    def __init__(self, size):
        """Initialization of a function new_square.

        Argumnets:
            size (int): is The size of the new_square.
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
