#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    try:
        if len(args) < 3:
            result = fct(args[0], args[1])
            return (result)
    except Exception as e:
        print("Exception: {}".format(e), file=sys.stderr)
        return (None)
