#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    b_dictionary = a_dictionary.copy()
    for k, i in a_dictionary.items():
        b_dictionary[k] = i * 2
    return b_dictionary
