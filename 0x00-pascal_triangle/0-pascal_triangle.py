#!/usr/bin/python3
"""
pascal_triangle module
"""


def pascal_triangle(n):
    """
    the pascal_triangle function
    takes an integer and returns
    equivalent pascal triangle in form
    of a list of lists
    if the integer passed is less or
    equal to zero, an empty
    list is returned
    """
    triangle = []
    if n <= 0:
        return triangle
    for i in range(n + 1):
        if i == 0:
            triangle.append([1])
        elif i == 1:
            triangle.append([1, 1])
        else:
            temp = []
            idx = 0
            temp.append(1)
            while idx <= len(triangle[-1]) - 2:
                temp.append(triangle[-1][idx] + triangle[-1][idx + 1])
                idx += 1
            temp.append(1)
            triangle.append(temp)
    return triangle
