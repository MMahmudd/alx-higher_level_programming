def read_file(filename=""):
    """Function that reads a text file and prints its content."""

    with open(filename, "r", encoding="utf-8") as f:
        text_file = f.read()
        print(text_file, end="")
