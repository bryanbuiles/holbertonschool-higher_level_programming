#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    try:
        for arg in args:
            result = fct(*args)
            return (result)
    except Exception as e:
        print("Exception: {}".format(e), file=sys.stderr)
        return (None)
