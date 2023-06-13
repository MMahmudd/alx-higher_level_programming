def read_file(filename=""):
    """Function that reads a text file and prints its content."""


    with open(filename) as f:
        text = f.read()
        print(text, end="")
