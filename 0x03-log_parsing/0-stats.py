#!/usr/bin/python3
"""
Write a script that reads stdin line by line and computes metrics:

* Input format: var = "GET /projects/260 HTTP/1.1"
    <IP Address> - [<date>] <var> <status code> <file size>
    (if the format is not this one, the line must be skipped)
* After every 10 lines and/or a keyboard interruption (CTRL + C),
    print these statistics from the beginning:
        Total file size: File size:
            <total size> is the sum of all previous <file size>.
        Number of lines by status code:
            possible status code:
                200, 301, 400, 401, 403, 404, 405 and 500.
* if a status code doesn’t appear or is not an integer, don’t print anything.
* format: <status code>: <number>
* status codes should be printed in ascending order.
"""
import sys
import os
import signal
import re


def is_status(status_code: int) -> bool:
    """Tells if a code is a status code.

    Args:
        status_code (int): the value of status.

    Returns:
        bool: True if is a status.
    """
    status_list = [
        200, 301, 400,
        401, 403, 404,
        405, 500]
    if status_code in status_list:
        return True
    return False


def print_statistics(input: str):
    """
    prints Total file size and Number of lines by status code
    if the format is not as bellow, the line must be skipped.

    Args:
        input (str): follows this format :<IP Address> -
            [<date>] "GET /projects/260 HTTP/1.1"
            <status code> <file size>.
    """
    total_size = 0
    _stats = {
        '200': 0, '301': 0, '400': 0,
        '401': 0, '403': 0, '404': 0,
        '405': 0, '500': 0}
    if input != "" or input != "\t":
        for line in input.split("\t"):
            if line != "":
                split_l1 = line.split("\"")
                split_l2 = split_l1[2].split()
                total_size += int(split_l2[1])
                st = split_l2[0]
                if st in _stats.keys():
                    _stats[st] += 1
        print("File size: {}".format(total_size))
        for k in _stats:
            if _stats[k] != 0:
                print("{}: {}".format(k, _stats[k]))


if __name__ == '__main__':
    max_lines = 10
    counter = min_val = 0
    buffer = ""
    try:
        while (True):
            line = input()
            counter += 1
            buffer += line + "\t"
            if counter == max_lines:
                counter = min_val
                print_statistics(buffer)
                buffer = ""
    except (EOFError, KeyboardInterrupt):
        print_statistics(buffer)
        buffer = ""
