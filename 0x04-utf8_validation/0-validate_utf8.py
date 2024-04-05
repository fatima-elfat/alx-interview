#!/usr/bin/python3
"""
Task 0: UTF-8 Validation.
Write a method that determines if a given
data set represents a valid UTF-8 encoding.
* A character in UTF-8 can be 1 to 4 bytes long.
* The data set can contain multiple characters.
* The data will be represented by a list of integers.
* Each integer represents 1 byte of data,
    therefore you only need to handle the 8
    least significant bytes of each integer.
"""
from itertools import takewhile


def generatebytes(data):
    """
    generates bytes.
    """
    for byte in data:
        r = []
        mask = 1 << 8
        while mask:
            mask >>= 1
            r.append(bool(byte & mask))
        # Yield is used in Python generators.
        # We should use yield when we want to
        # iterate over a sequence, but don’t want
        # to store the entire sequence in memory.
        yield r


def validUTF8(data):
    """
    determines if a given data set is valid UTF-8 encoding.
    Returns: True if data is a valid UTF-8 encoding, else return False
    """
    r = True
    bytes = generatebytes(data)
    for byte in bytes:
        if byte[0] == 0:
            continue
        sum_ = sum(takewhile(bool, byte)) - 1
        if sum_ <= 0 or sum_ >= 3:
            r = False
        for i in range(sum_):
            try:
                # using yield generates the next
                byte = next(bytes)
            except Exception:
                r = False
            if byte[0:2] != [1, 0]:
                r = False
    return r
