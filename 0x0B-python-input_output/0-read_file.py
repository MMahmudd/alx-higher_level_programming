def read_file(filename=""):
    """Function that reads a text file and prints its content
    Read the entire file content. Print the content to
    stdout without adding an extra newline character"""

    with open(filename, "r", encoding="utf-8") as f_object:
        text = f_object.read()
        print(text, end="")
