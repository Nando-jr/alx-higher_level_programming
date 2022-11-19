#!/usr/bin/python3
"""text_indentation module"""


def text_indentation(text):
    """function that prints a text with 2 new lines
    after each of these characters: ., ? and :
    Args:
        text: string
    """
    if type(text) != str:
        raise TypeError("text must be a string")

    n = text[:]
    for m in ["?", ":", "."]:
        txt = n.split(m)
        n = ""
        for s in txt:
            s = s.strip(" ")
            if n == "":
                n = s + m
            else:
                n + "\n\n" + s + m
    print(n[:-3], end="")
