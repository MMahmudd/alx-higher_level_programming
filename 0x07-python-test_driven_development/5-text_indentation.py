#!/usr/bin/python3
# 5-text_indentation.py
"""Defination of a function text-indentation."""


def text_indentation(text):
    """Printing text with two new_lines after each '.', '?', and ':'.

    Argumnets:
        text (string): The text to be printed.
    Raise:
        TypeError: If text isn't a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    cc = 0
    while cc < len(text) and text[cc] == ' ':
        cc += 1

    while cc < len(text):
        print(text[cc], end="")
        if text[cc] == "\n" or text[cc] in ".?:":
            if text[cc] in ".?:":
                print("\n")
            cc += 1
            while cc < len(text) and text[cc] == ' ':
                cc += 1
            continue
        cc += 1
