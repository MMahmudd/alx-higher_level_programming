#!/usr/bin/python3
"""Defines a class named Rectangle."""


class Rectangle:
    """Represents Rectangle.

    Attribute:
        number_of_instances (integers): A number of instances of a Rectangle.
    """

    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """Initialiation of a new_Rectangle.

        Arguments:
            width (int): Width of a new_rectangle.
            height (int): Height of a new_rectangle.
        """
        type(self).number_of_instances += 1
        self.width = width
        self.height = height

    @property
    def width(self):
        """Getter/setter width of Rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Getter/setter height of Rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Returns area of Rectangle."""
        return (self.__width * self.__height)

    def perimeter(self):
        """Returns perimeter of Rectangle."""
        if self.__width == 0 or self.__height == 0:
            return (0)
        return ((self.__width * 2) + (self.__height * 2))

    def __str__(self):
        """Returns print that's representation of a Rectangle.

        Representing a rectangle using this # char.
        """
        if self.__width == 0 or self.__height == 0:
            return ("")

        rect_char = []
        for ii in range(self.__height):
            [rect_char.append('#') for jj in range(self.__width)]
            if ii != self.__height - 1:
                rect_char.append("\n")
        return ("".join(rect_char))

    def __repr__(self):
        """Returns  string that's  representation of of Rectangle."""
        rect_char = "Rectangle(" + str(self.__width)
        rect_char += ", " + str(self.__height) + ")"
        return (rect_char)

    def __del__(self):
        """Prints a message for the deleted of a Rectangle."""
        type(self).number_of_instances -= 1
        print("Bye rectangle...")
