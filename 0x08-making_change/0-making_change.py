#!/usr/bin/python3
"""0. Change comes from within """


def makeChange(coins, total):
    """Return: fewest number of coins needed to meet total"""
    if total <= 0:
        return 0
    if len(coins) <= 0:
        return -1
    coins.sort()
    pile = len(coins)-1
    change = 0
    while(pile >= 0):
        while(coins[pile] < total):
            total -= coins[pile]
            change += 1
        pile -= 1
    return change
