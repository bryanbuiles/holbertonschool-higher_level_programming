#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    tuple_a += (0, 0)
    tuple_b += (0, 0)
    add_tuple1 = (tuple_a[0] + tuple_b[0])
    add_tuple2 = (tuple_a[1] + tuple_b[1])
    add_tuples = (add_tuple1, add_tuple2)
    return(add_tuples)
