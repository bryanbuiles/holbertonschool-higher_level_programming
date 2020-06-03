#!/usr/bin/python3
""" add items """
import sys

load_from_json_file = __import__('8-load_from_json_file').load_from_json_file
save_to_json_file = __import__('7-save_to_json_file').save_to_json_file

try:
    milist = load_from_json_file('add_item.json')
except FileNotFoundError:
    milist = []
for i in sys.argv[1:]:
    milist.append(i)
save_to_json_file(milist, 'add_item.json')
