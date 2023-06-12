#!/usr/bin/python3
"""module named 2-is_same_class.py with a method
     named is_same_class
"""


def is_same_class(obj, a_class):
    """implementation of method that return true
    when object is an instance of a class.

    Argumnets:
             obj (any): is object to be checked.
             a_class (type): is class_ match the type of obj

   Return:
         If obj is an instance of a_class - True.
        else - False.
    """
    if type(obj) == a_class:
        return True
    return False
