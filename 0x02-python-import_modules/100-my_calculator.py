#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    import calculator_1 as cal
    if (len(argv) != 4):
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    else:
        a = int(argv[1])
        b = int(argv[3])
        if (argv[2] not in ('+', '-', '*', '/')):
            print("Unknown operator. Available operators: +, -, * and /")
            exit(1)
        elif (argv[2] == '+'):
            print("{:d} + {:d} = {:d}".format(a, b, cal.add(a, b)))
        elif (argv[2] == '-'):
            print("{:d} - {:d} = {:d}".format(a, b, cal.sub(a, b)))
        elif (argv[2] == "*"):
            print("{:d} * {:d} = {:d}".format(a, b, cal.mul(a, b)))
        elif (argv[2] == '/'):
            print("{:d} / {:d} = {:d}".format(a, b, cal.div(a, b)))
