#!/usr/bin/python3
""" write """


def write_file(filename="", text=""):
    """
    Keyword Arguments:
        filename {object} -- file text (default: {""})
        text {str} -- string to write (default: {""})

    Returns:
        [int] -- number of words
    """
    with open(filename, mode="w", encoding="utf-8") as f:
        f.write(text)
    with open(filename, mode="r", encoding="utf-8") as f:
        count = 0
        x = f.read()
        for words in x:
            for letters in words:
                count += 1
        return count
