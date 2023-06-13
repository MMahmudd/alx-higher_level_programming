#!/usr/bin/python3
"""A module that contained a function named save_to_json_file"""
import json


def save_to_json_file(my_obj, filename):
    """Writting an Object to a text_file use JSON_repersentation.

    Arguments:
        my_obj (type): is an object writting to text_file.
        filename (str): is name of a file.

    Return:
        type: is JSON_representation.
    """

    with open(filename, 'w', encoding="utf-8") as f_object:
        json_obj = json.dumps(my_obj)
        f_object.write(json_obj)
        f_object.close()
