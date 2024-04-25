#!/usr/bin/python3
"""
Task 0. Rotate 2D Matrix.
"""


def rotate_2d_matrix(matrix):
    """
    Given an n x n 2D matrix, rotate it 90 degrees clockwise.
    """
    min = 0
    max = len(matrix)
    # new_matrix = [[0] * max for i in range(max)]
    old_matrix = [list(line) for line in matrix]
    max -= 1
    try:
        for i in range(max + 1):
            for j in range(max + 1):
                s = max - i
                matrix[j][s] = old_matrix[i][j]
    except Exception:
        pass
