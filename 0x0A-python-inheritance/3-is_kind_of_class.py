#!/usr/bin/python3
"""Defines a class named 3-is_kind_of_class.py
   and inherited_ class checking_function."""


def is_kind_of_class(obj, a_class):
    """Checking if an object is an_instance or
    an_ inherited_instance of a class.

    Arguments:
        obj (any): is object to be checked.
        a_class (type): is class to be matched the type of obj to.
    Return:
        If obj is an_instance or an_inherited instance of a_class - True.
        else - False.
    """
    if isinstance(obj, a_class):
        return True
    return False
