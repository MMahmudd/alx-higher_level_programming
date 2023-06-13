#!/usr/bin/python3
"""A module that's loaded, adding and saving an argument to a Python_list"""
from sys import argv


load_from_json_fil = __import__('6-load_from_json_file').load_from_json_file
save_to_json_fil = __import__('5-save_to_json_file').save_to_json_file

try:
    json_list = load_from_json_fil('add_item.json')
except (ValueError, FileNotFoundError):
    json_list = []

for item in argv[1:]:
    json_list.append(item)

save_to_json_fil(json_list, 'add_item.json')
