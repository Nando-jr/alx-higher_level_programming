#!/usr/bin/python3
def element_at(my_list, idx):
    for n in my_list:
        if idx == my_list.index(n):
            return n
        elif idx < 0 or idx > len(my_list):
            return None
