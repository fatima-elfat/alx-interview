#!/usr/bin/python3
"""
Task 0. Island Perimeter.
Prototype: def island_perimeter(grid).
grid is rectangular, with its width and height not exceeding 100
The grid is completely surrounded by water
There is only one island (or nothing).
The island doesn’t have “lakes” (water inside that isn’t
connected to the water surrounding the island).
"""


def island_perimeter(grid: list) -> int:
    """checks if an island exists and returns the perimeter.

    Args:
        grid (list): list of list of integers
            0 represents water
            1 represents land
            Each cell is square, with a side length of 1
            Cells are connected horizontally/vertically.

    Returns:
        int: the perimeter of the island.
    """
    r = 0
    lenght = len(grid)
    for i in range(lenght):
        for j in range(lenght):
            if grid[i][j] == 0:
                continue
            r += 4
            if i > 0 and grid[i-1][j]:
                r -= 2
            if j > 0 and grid[i][j-1]:
                r -= 2
    return r
