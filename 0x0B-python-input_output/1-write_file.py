#!/usr/bin/python3
"""Module that contains a function named write_file"""


def write_file(filename="", text=""):
    """Writes a string to a text_file (UTF8) and returing a number
    of characters that is written.

    Argumnets:
        filename (str, optional): is name of the file. "".
        text (str, optional): is string of text to be written to file.

    Return:
        int: is number of char that written to text_file.
    """
    with open(filename, 'w', encoding="utf-8") as f_object:
        """A method that returns a number of char tha's written to file."""
        return f_object.write(text)
