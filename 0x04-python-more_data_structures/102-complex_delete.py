#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    klist = list(a_dictionary.keys())
    for n in klist:
        if value == a_dictionary.get(n):
            del a_dictionary[n]
    return a_dictionary
