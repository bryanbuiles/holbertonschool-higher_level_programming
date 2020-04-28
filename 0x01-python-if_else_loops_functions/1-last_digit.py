#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
j = number
lastdigit = j % 10
if (number < 0):
    j = -1 * number
    lastdigit = (j % 10) * -1
word = "Last digit of"
if (lastdigit > 5):
    print("{} {} is {} and is greater than 5".format(word, number, lastdigit))
elif (lastdigit == 0):
    print("{} {} is {} and is 0".format(word, number, lastdigit))
else:
    print("{} {} is {} and is less than 6 and not 0".format(
        word, number, lastdigit))
