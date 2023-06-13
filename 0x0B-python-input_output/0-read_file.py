def read_file(filename=""):
    """Function that reads a text file and prints its content."""

    with open(filename, "r", encoding="utf-8") as file:
        # Read the entire file content
        text = file.read()
        print(text, end="")
