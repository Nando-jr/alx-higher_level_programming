#!/usr/bin/python3
def no_c(my_string):
    ch = ""
    for s in my_string:
        if s != 'c' and s != 'C':
            ch = ch + s
    return (ch)
