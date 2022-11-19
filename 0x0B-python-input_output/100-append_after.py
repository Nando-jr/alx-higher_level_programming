#!/usr/bin/python3
"""append_after"""


def append_after(filename="", search_string="", new_string=""):
    """function that inserts a line of text to a file,
    after each line containing a specific string
    """
    a = []
    with open(filename, 'r', encoding="utf-8") as file:
        for ln in file:
            a += [ln]
            if ln.find(search_string) != -1:
                a += [new_string]
    with open(filename, 'w', encoding="utf-8") as file:
        file.write("".join(a))
