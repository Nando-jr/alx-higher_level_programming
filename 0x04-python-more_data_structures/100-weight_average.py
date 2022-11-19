#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0
    r1 = 0
    r2 = 0
    for a, b in my_list:
        r1 += a * b
        r2 += b
    return (r1 / r2)
