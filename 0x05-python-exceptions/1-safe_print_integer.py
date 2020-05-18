#!/usr/bin/python3
def safe_print_integer(value):
    try:
        stri = str(value)
        if any(char.isdigit() for char in stri):
            print("{:d}".format(value))
            return (True)
        else:
            return (False)
    except SyntaxError:
        pass
