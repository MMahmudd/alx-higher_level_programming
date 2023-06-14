#!/usr/bin/python3
"""A module that's defined  a class to reads
from standard input and computes metrics.

After_every ten _ines or the input from a keyboard
interruption CTRL + C,
printing as following statistically:
    - Total_file size up_to that point.
    - Count_of_read status code up_to that point.
"""


def print_stats(size, status_code):
    """Printing accumulat_metrics.

    Argumnets:
        size (int): is the accumulated read_file size.
        status_codes (dict): is the accumulated count_of_status.
    """
    print("File size: {}".format(size))
    for keey in sorted(status_code):
        print("{}: {}".format(keey, status_code[keey]))


if __name__ == "__main__":
    import sys

    size = 0
    status_code = {}
    valid_codes = ['200', '301', '400', '401', '403', '404', '405', '500']
    counts = 0

    try:
        for lines in sys.stdin:
            if counts == 10:
                print_stats(size, status_code)
                counts = 1
            else:
                counts += 1

            lines = lines.split()

            try:
                size += int(lines[-1])
            except (IndexError, ValueError):
                pass

            try:
                if lines[-2] in valid_codes:
                    if status_code.get(lines[-2], -1) == -1:
                        status_code[lines[-2]] = 1
                    else:
                        status_code[lines[-2]] += 1
            except IndexError:
                pass

        print_stats(size, status_code)

    except KeyboardInterrupt:
        print_stats(size, status_code)
        raise
