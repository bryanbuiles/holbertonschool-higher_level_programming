#!/usr/bin/python3
def print_last_digit(number):
    j = number
    lastdigit = j % 10
    if (number < 0):
        j = -1 * number
        lastdigit = (j % 10)
    print(lastdigit, end="")
    return (lastdigit)
