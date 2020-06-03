#!/usr/bin/python3
""" append write """


def append_write(filename="", text=""):
    """
    Keyword Arguments:
        filename {object} -- file text (default: {""})
        text {str} -- string to write (default: {""})

    Returns:
        [int] -- number of words
    """
    with open(filename, mode="a", encoding="utf-8") as f:
        f.write(text)
        return(len(text))
