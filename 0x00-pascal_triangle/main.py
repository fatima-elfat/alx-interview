#!/usr/bin/python3
"""
0-main
"""
pascal_triangle = __import__('0-pascal_triangle').pascal_triangle

def print_triangle(triangle):
    """
    Print the triangle
    """
    for row in triangle:
        print("[{}]".format(",".join([str(x) for x in row])))


if __name__ == "__main__":
    print("for -1")
    print_triangle(pascal_triangle(-1))
    print("for 0")
    print_triangle(pascal_triangle(0))
    print("for 1")
    print_triangle(pascal_triangle(1))
    print("for 5")
    print_triangle(pascal_triangle(5))
    print("for 10")
    print_triangle(pascal_triangle(10))
