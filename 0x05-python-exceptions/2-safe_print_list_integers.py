#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    conta = 0
    try:
        for i in range(x):
            if isinstance(my_list[i], int):
                print("{:d}".format(my_list[i]), end="")
                conta += 1
        print("")
        return conta
        print()
    except (TypeError, ValueError):
        pass
