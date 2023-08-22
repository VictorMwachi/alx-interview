#!/usr/bin/python3
"""0. Change comes from within """


def makeChange(coins, total):
  """Return: fewest number of coins needed to meet total"""
  if total <= 0:
    return 0
  if coins.len() <= 0:
    return -1
  
