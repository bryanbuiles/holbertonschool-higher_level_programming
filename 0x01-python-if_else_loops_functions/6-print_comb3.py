#!/usr/bin/python3
for i in range(0, 100):
    p = i % 10
    j = i // 10
    if p == j:
        continue
    elif(j == 8 and p == 9):
        print(j, p, sep="")
    elif (j < p):
        print(j, p, sep="", end=", ")
