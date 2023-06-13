def read_file(filename=""):
    # Open the file in read mode with UTF-8 encoding
    with open(filename, "r", encoding="utf-8") as file:
        # Iterate over each line in the file
        for line in file:
            # Print each line to stdout without
            #adding an extra newline character
            print(line, end="")
