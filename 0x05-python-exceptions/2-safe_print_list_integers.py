#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    count = 0
    try:
        lista = []
        for j in my_list:
            if type(j) == int:
                lista.append(j)
        listat = list(lista[:x])
        for i in listat:
            print("{:d}".format(i), end="")
            count += 1
        print()
        return(count)
    except (ValueError, TypeError):
        pass
