#!/usr/bin/python3
"""a module that's defined a class text_file ins function."""


def append_after(filename="", search_string="", new_string=""):
    """Insertting text after each line_containing  string in a file.

    Argumnets:
        filename (str): is the name_file.
        search_string (str): is the string to be searched
        for within the file.
        new_string (str): is the string to be inserted.
    """
    texts = ""
    with open(filename) as r_object:
        for lines in r_object:
            texts += lines
            if search_string in lines:
                texts += new_string
    with open(filename, "w") as w_object:
        w_object.write(texts)
