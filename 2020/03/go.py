#!/usr/bin/env python3
#15 - 32

import sys
from math import prod

def get_cell(grid, coord):
    x, y = coord[0] % len(grid[0]), coord[1]
    return grid[y][x]

def count(lines, slope):
    c, i = 0, 0
    while True:
        if i*slope[1] >= len(lines):
            break
        c += get_cell(lines, (i*slope[0], i*slope[1])) == '#'
        i += 1
    return c

if __name__=='__main__':
    lines = []
    for line in sys.stdin.readlines():
        lines.append(list(line.strip()))

    slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
    tree_counts = map(lambda s: count(lines, s), slopes)
    print(prod(tree_counts))
