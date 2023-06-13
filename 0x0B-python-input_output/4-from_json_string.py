#!/usr/bin/python3
"""A module that's contained a function named from_json_string"""
import json


def from_json_string(my_str):
    """Returning an object of Python data structure by a JSON string.

    Argumnets:
        my_str (str): is json_object to converting to Python_object.

    Return:
        type: is Python_object.
    """

    return json.loads(my_str)
