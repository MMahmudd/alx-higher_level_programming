#!/usr/bin/python3
"""Definition of a function add_attribute
             that's adding attributes to an objects."""


def add_attribute(obj, att, value):
    """Adding a new_attribute to an_object if_possible.

    Argumnets:
        obj (any): is an_object to add an_attribute to.
        att (str): is a name of attribute to ad to obj.
        value (any): is a value of att.
    Raise:
        TypeError: If an_ attribute can't be added.
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, att, value)
