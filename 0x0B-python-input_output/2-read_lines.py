#!/usr/bin/python3
""" number of lines """


def read_lines(filename="", nb_lines=0):
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
            print(x, end="")
            if linenumber == nb_lines:
                break
