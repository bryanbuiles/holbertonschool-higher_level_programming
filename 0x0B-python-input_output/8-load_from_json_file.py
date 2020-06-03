#!/usr/bin/python3
"""save json
"""
import json


def load_from_json_file(filename):
    """ write json in a file """
    with open(filename, mode="r", encoding="UTF-8") as f:
        return json.load(f)
