#!/usr/bin/python3
def remove_char_at(str, n):
    c = str
    if n < 0:
        return c
    c = c[:n] + "" + c[n + 1:]
    return c
