#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    b_dictionary = a_dictionary.copy()
    if value:
        for k, i in b_dictionary.items():
            if i == value:
                del a_dictionary[k]
        return a_dictionary
    else:
        return(b_dictionary)
