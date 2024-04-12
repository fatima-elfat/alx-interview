#!/usr/bin/env python3
"""
The N queens puzzle is the challenge of placing
N non-attacking queens on an N×N chessboard.
Write a program that solves the N queens problem.

* Usage: nqueens N
    If the user called the program with the wrong number
        of arguments, print Usage: nqueens N, followed
        by a new line, and exit with the status 1.
    where N must be an integer greater or equal to 4.
    If N is not an integer, print N must be a number,
        followed by a new line, and exit with
        the status 1.
    If N is smaller than 4, print N must be at least 4,
        followed by a new line, and exit with the status 1
* The program should print every possible solution to the problem
    One solution per line
    Format: see example: 0-nqueens.py 4
        [[0, 1], [1, 3], [2, 0], [3, 2]]
        [[0, 2], [1, 0], [2, 3], [3, 1]]
    You don’t have to print the solutions in a specific
        order
* You are only allowed to import the sys module
"""
import sys


global prev
global results


def get_solution(n, queen):
    """
    get_solution,

    Returns:
        bool: True to print or false if queen can't be placed.
    """
    for i in range(1, n + 1):
        a = True
        for j in range(1, queen):
            if prev[j] == i or \
                    abs(prev[j] - i) == abs(j - queen):
                a = False
                break
            a = True
        if a:
            prev[queen] = i
            if queen == n:
                solution = []
                for i in range(1, n + 1):
                    solution.append([i - 1, prev[i] - 1])
                results.append(solution)
            else:
                get_solution(n, queen + 1)
    return results


if len(sys.argv) != 2:
    print("Usage: nqueens N")
    sys.exit(1)
try:
    N = int(sys.argv[1])
except Exception:
    print("N must be a number")
    sys.exit(1)
if N < 4:
    print("N must be at least 4")
    sys.exit(1)
results = []
prev = [0]*(N + 1)
lists = get_solution(N, 1)
for result in lists:
    print(result)
