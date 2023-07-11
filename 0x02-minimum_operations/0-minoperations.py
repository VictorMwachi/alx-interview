#!/usr/bin/python3
"""
0. Minimum Operations
"""

import math


def minOperations(n):
    """
    calculates the fewest number of operations needed
    to result in exactly n H characters in the file
    """
    if n < 2:
        return 0
    while n % 2 == 0:
        prime_list.append(2)
        n /= 2
        for i in range(3, int(math.sqrt(n)) + 1, 2):
            while n % i == 0:
                prime_list.append(i)
                n /= i
        if n > 2:
            prime_list.append(i)
    return sum(prime_list)
