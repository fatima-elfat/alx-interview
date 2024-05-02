#!/usr/bin/python3
"""
Task 0. Change comes from within.
Prototype: def makeChange(coins, total)
"""


def makeChange(coins: list, total: int) -> int:
    """Given a pile of coins of different values,
    determine the fewest number of coins needed to meet a given amount total.

    Args:
        coins (list): the values of the available coins.
        total (int): the total.

    Returns:
        int: the number of used coins.
    """
    r = 0
    coins.sort(reverse=True)
    for val in coins:
        while (total > 0 and total >= val):
            r += 1
            total -= val
    if (total > 0):
        r = -1
    return r
