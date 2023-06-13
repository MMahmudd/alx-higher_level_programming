#!/usr/bin/python3
def read_file(filename=""):
    """"A function that used to read a text_file
    and print out its content"""

    with open(filename"r", encoding="UTF-8") as ff:
        text_file = ff.read()
        print(text_file, end="")
