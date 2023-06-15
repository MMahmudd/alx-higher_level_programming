#!/usr/bin/python3
"""Definition of class named a square."""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Representation_square."""

    def __init__(self, size, x=0, y=0, id=None):
        """Initialization a new_Square.

        Arguments:
            size (int): is the size of new_Square.
            x (int): is the x_coordinate of new_Square.
            y (int): is the y_coordinate of new_Square.
            id (int): is the identity of new_Square.
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Getter/setter the size_of_Square."""
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Update_Square.

        Argumnets:
            *args (ints): New_attribute_values.
                - 1st argument_represents id_attribute
                - 2nd argument_represents size_attribute
                - 3rd argument_represents x_attribute
                - 4th argument represents y_attribute
            **kwargs (dict): New_key/value pairs_of_attributes.
        """
        if args and len(args) != 0:
            a = 0
            for arg in args:
                if a == 0:
                    if arg is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = arg
                elif a == 1:
                    self.size = arg
                elif a == 2:
                    self.x = arg
                elif a == 3:
                    self.y = arg
                a += 1

        elif kwargs and len(kwargs) != 0:
            for k, v in kwargs.items():
                if k == "id":
                    if v is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = v
                elif k == "size":
                    self.size = v
                elif k == "x":
                    self.x = v
                elif k == "y":
                    self.y = v

    def to_dictionary(self):
        """Returning the dictionary_representation of the_Square."""
        return {
            "id": self.id,
            "size": self.width,
            "x": self.x,
            "y": self.y
        }

    def __str__(self):
        """Returning the print() and str() representation_of_Square."""
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y,
                                                 self.width)
