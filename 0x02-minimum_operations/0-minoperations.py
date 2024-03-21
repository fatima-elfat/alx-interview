#!/usr/bin/python3
"""
Task 0: Minimum Operations.
"""


def minOperations(n):
    """
    calculates the number of operation needed
    to result in exactly n H characters in the file.
    """
    r = copied = 0
    now_val = 1
    while now_val < n:
        if n % now_val == 0:
            copied = now_val
            r = r + 1
        now_val = now_val + copied
        r = r + 1
    return r
