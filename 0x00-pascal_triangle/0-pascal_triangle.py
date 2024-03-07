#!/usr/bin/python3
"""
pascal triangle
"""


def binomialCoef(n, j):
    """
    Calculates the binominal coeffiencent.
    C(n, j) = n! / (n-j)! * j!
    with C(n,j) = C(n, n-j) if j> n - j
    Returns: the value of the coefficient in line n (row) in column j.
    """
    coef = 1
    if (n > n - j):
        j = n - j
    for i in range(j):
        coef *= ((n - i) / (i + 1))
    return (int(coef))

def pascal_triangle(n):
    """
    create a Pascal triangle.
    Returns: a list of line of triangle.
    """
    result = []
    if n <= 0 or type(n) is not int:
        return result
    for i in range(n):
        line = []
        m = i + 1
        for j in range(m):
            line.append(binomialCoef(i, j))
        result.append(line)
    return result
