#!/usr/bin/python3
"""A module that contained a function named append_write"""


def append_write(filename="", text=""):
    """Appending or adding a string to a text_ile (UTF8)
    and returning the number of characters that's added.

    Argumnets:
        filename (str, optional): is named of the file. default to "".
        text (str, optional): is string of text_write to file. default to "".

    Return:
        int: is number of characters added to file.
    """
    with open(filename, 'a', encoding="utf-8") as f_object:
        """This method returns the number_ characters added to a file."""
        return f_object.write(text)
