#!/usr/bin/python3
"""Defines a class of a  Rectangle."""


class Rectangle:
    """Represents Rectangle.

    Attribute:
        number_of_instances (int): A number of Rectangle's instances.
        print_symbol (any): The symbol is used for representation of string.
    """

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Initialization of a new_rectangle.

        Argumnets:
            width (int): Width of a new_rectangle.
            height (int): Height of a new_rectangle.
        """
        type(self).number_of_instances += 1
        self.width = width
        self.height = height

    @property
    def width(self):
        """Getter/setter A width of rectangle."""
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
        """Getter/setter A height of rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Returns an area of rectangle."""
        return (self.__width * self.__height)

    def perimeter(self):
        """Returns a perimeter of a rectangle."""
        if self.__width == 0 or self.__height == 0:
            return (0)
        return ((self.__width * 2) + (self.__height * 2))

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Returns rectangle with a greater_area.

        Argumnets:
            rect_1 (Rect): First rectangle.
            rect_2 (Rect): Second rectangle.
        Raise:
            TypeError: If either of rect_1 or rect_2 isn't a rectangle.
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return (rect_1)
        return (rect_2)

    def __str__(self):
        """Returns print that's representation of a rectangle.

        Returns A rectangle using this # char.
        """
        if self.__width == 0 or self.__height == 0:
            return ("")

        rect_char = []
        for ii in range(self.__height):
            [rect_char.append(str(self.print_symbol))
             for jj in range(self.__width)]
            if ii != self.__height - 1:
                rect_char.append("\n")
        return ("".join(rect_char))

    def __repr__(self):
        """Returns  string that's representation of Rectangle."""
        rect_char = "Rectangle(" + str(self.__width)
        rect_char += ", " + str(self.__height) + ")"
        return (rect_char)

    def __del__(self):
        """Prints a message for the  deleted of rectangle."""
        type(self).number_of_instances -= 1
        print("Bye rectangle...")
