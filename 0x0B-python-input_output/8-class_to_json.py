#!/usr/bin/python3
"""A module that's contained a function named class_to_json"""


def class_to_json(obj):
    """Returning the dict_description with simple data_structure,
    (list, dictionary, is str, int and bool for JSON_serialization,
    of objects.

    Arguments:
        obj (MyClass):is an object.

    Return:
        dict: is dictionary.
    """
    return obj.__dict__
