#!/usr/bin/python3
"""define a class that provides a function for checking
              inherted class.
              """


def inherits_from(obj, a_class):
    """Checking if an_object is an inherited_instance of a class.

    Arguments:
        obj (any):is an object to be checked.
        a_class (type): is a class to be  matched a type of obj to.
    Return:
        If obj is an_inherited_instance of a_class - True.
        else - False.
    """
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return False
