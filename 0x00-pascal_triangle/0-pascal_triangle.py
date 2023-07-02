#!/usr/bin/python3
def pascal_triangle(n):
    triangle = []
    if n <= 0:
        return triangle
    for i in range(1, n + 1):
        if i == 1:
            triangle.append([1])
            triangle.append([1,1])
        else:
            temp = []
            idx = 0
            temp.append(1)
            while idx + 1 <= len(triangle[-1]) - 1:
                temp.append(triangle[-1][idx] + triangle[-1][idx + 1])
                idx += 1
            temp.append(1)
            triangle.append(temp)
    return triangle
