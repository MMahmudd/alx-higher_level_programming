#!/usr/bin/python3
"""A module that contained a function named read_file"""


def read_file(filename=""):
    """Reads a text_file and printout to stdout.

    Argumnets:
        filename (str, optional): is named of text_file to read.
        Default to "".
    """
    with open(filename, 'r', encoding="utf-8") as f_object:
        read_text_file = f_object.read()
        print(read_text_file, end='')
