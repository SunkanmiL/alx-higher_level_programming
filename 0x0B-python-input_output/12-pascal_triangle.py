#!/usr/bin/python3
"""Defines a Pascal Triangle"""


def pascal_triangle(n):
    """Returns a list of lists of integers representing the Pascal's triangle
    of n
    Args:
        n (int): number of rows
    """
    if n <= 0:
        return []

    res = [[1]]
    for _ in range(n - 1):
        temp = [0] + res[-1] + [0]
        new_row = []
        for j in range(len(res[-1]) + 1):
            new_row.append(temp[j] + temp[j + 1])
        res.append(new_row)
    return res
