#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    if(len(argv) == 1):
        print("0")
    elif(len(argv) > 1):
        r = int(argv[1])
        for i in range(len(argv)):
            if (i > 1):
                p = int(argv[i])
                r = r + p
        print("{}".format(r))
