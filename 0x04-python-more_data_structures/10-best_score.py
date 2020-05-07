#!/usr/bin/python3
def best_score(a_dictionary):
    m = 0
    if a_dictionary:
        for k, i in a_dictionary.items():
            if i > m:
                m = i
                j = k
        return (j)
    return (None)
