#!/usr/bin/python3
def read_file(filename=""):
    """ A function that reads a text_file and prints its contains"""

    with open(filename) as f:
        text = f.read()
        print(text, end="")
