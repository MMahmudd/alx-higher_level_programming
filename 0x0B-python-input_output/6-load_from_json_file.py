#!/usr/bin/python3
"""A module that's contained a function named load_from_json_file"""
import json


def load_from_json_file(filename):
    """Creating an object of a “JSON_file”.

    Argumnets:
        filename (str): is name of a file.

    Return:
        object: is Object.
    """
    with open(filename, 'r', encoding="utf-8") as f_object:
        return json.load(f_object)
