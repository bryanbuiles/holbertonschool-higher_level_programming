#!/usr/bin/python3
"""
    text_indentation module
    text_indentation: function that prints my name
    Return: nothing
"""


def text_indentation(text):
    """ Function that prints part of the text
        text(str): input text
    """
    co = 0
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    for i in text:
        if i in ['.', '?', ':']:
            if text[co + 1] == " ":
                text = text[:co + 1] + text[co + 2:]
        else:
            co += 1
    for i in text:
        print(i, end="")
        if i in ['.', '?', ':']:
            print()
            print()
