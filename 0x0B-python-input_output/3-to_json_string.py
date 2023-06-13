#!/usr/bin/python3
"""A module that contained a function named to_json_string"""
import json


def to_json_string(my_obj):
    """Returnning the JSON represents of an object_string.

    Argumnets:
        my_obj (type): is an object to be examined.

    Return:
        str: is JSON represents of an object.
    """
    return json.dumps(my_obj)
