#!/usr/bin/python3
def multiple_returns(sentence):
    j = len(sentence)
    if j == 0:
        k = "None"
    else:
        k = sentence[0]
    tupla = (j, k)
    return(tupla)
