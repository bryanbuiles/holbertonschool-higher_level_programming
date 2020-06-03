#!/usr/bin/python3
""" number of lines """


def number_of_lines(filename=""):
    """
    Keyword Arguments:
        filename {file} -- file text (default: {""})

    Returns:
        [int] -- [line number]
    """
    with open(filename, mode="r", encoding="utf-8") as f:
        linenumber = 0
        while True:
            x = f.readline()
            if not x:
                break
            linenumber += 1
        return linenumber
