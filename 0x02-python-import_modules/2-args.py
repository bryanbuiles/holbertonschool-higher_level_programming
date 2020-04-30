#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    if (len(argv) == 1):
        print("0 arguments.")
    elif(len(argv) > 2):
        print("{:d} arguments:".format(len(argv) - 1))
    for i in range(len(argv)):
        if (len(argv) == 2 and i > 0):
            print("{:d} argument:".format(i))
            print("{:d}: {}".format(i, argv[i]))
        elif(len(argv) > 2 and i > 0):
            print("{:d}: {}".format(i, argv[i]))
