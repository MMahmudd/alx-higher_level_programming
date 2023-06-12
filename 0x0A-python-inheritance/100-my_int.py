#!/usr/bin/python3
"""Definition of a class named  MyInt
               that's inherited from int."""


class MyInt(int):
    """Inverting an integers operators == and !=."""

    def __eq__(self, value):
        """Overridding == opeartor by !=."""
        return self.real != value

    def __ne__(self, value):
        """Overriddig != operator by == ."""
        return self.real == value
