#!/usr/bin/python3
# 0-add_integer.py
"""Defination of an integer_addition funcs."""


def add_integer(a, b=98):
    """Returning an integer_addition of a& b.

    Float_args are type_casted to integere before_addition is performing.

    Raise:
        TypeError: If either of a or b is noInteger and nonFloat.
    """
    if ((not isinstance(a, int) and not isinstance(a, float))):
        raise TypeError("a must be an integer")
    if ((not isinstance(b, int) and not isinstance(b, float))):
        raise TypeError("b must be an integer")
    return (int(a) + int(b))
