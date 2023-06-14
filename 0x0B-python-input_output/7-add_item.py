#!/usr/bin/python3
"""A module Add all args to a Python_list and save_them to file.."""
import sys

if __name__ == "__main__":
    save_to_json_fil = __import__('5-save_to_json_file').save_to_json_file
    load_from_json_fil = \
        __import__('6-load_from_json_file').load_from_json_file

    try:
        item = load_from_json_fil("add_item.json")
    except FileNotFoundError:
        item = []
    item.extend(sys.argv[1:])
    save_to_json_fil(item, "add_item.json")
