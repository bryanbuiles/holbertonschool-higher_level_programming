#!/usr/bin/python3
"""
    Returns:
        [object] -- json object
"""
import json


def from_json_string(my_str):
    """ retur json object """
    return (json.loads(my_str))
