#!/usr/bin/python3
"""pascal_triangle"""


def pascal_triangle(n):
    """returns a list of lists of integers representing
    the Pascal’s triangle of n
    """
    if n <= 0:
        return []
    tr = [[1]]
    while len(tr) != n:
        a = tr[-1]
        b = [1]
        for j in range(len(a) - 1):
            b.append(a[j] + a[j + 1])
        b.append(1)
        tr.append(b)
    return tr
