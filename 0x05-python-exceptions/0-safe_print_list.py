#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    count = 0
    try:
        lista = list(my_list[:x])
        for i in lista:
            print(i, end="")
            count += 1
        print()
        return(count)
    except IndexError:
        pass
