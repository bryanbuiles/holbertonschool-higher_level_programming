#!/usr/bin/python3
"""0 read_file
"""


def read_file(filename=""):
    """
    Keyword Arguments:
        filename {file} -- text file (default: {""})
    """

    with open(filename, mode="r", encoding="utf-8") as f:
        x = f.read()
        print(x, end="")
