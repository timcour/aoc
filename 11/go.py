#!/usr/bin/env python3

import sys
from collections import Counter
from math import prod
from copy import deepcopy

def in_bounds(data, x, y):
    if x < 0 or x >= len(data):
        return False
    if y < 0 or y >= len(data[0]):
        return False
    return True

def inc_adjacent(lines, x, y, visited):
    for i in range(-1, 2):
        for j in range(-1, 2):
            xo, yo = x+i, y+j
            if not in_bounds(lines, xo, yo):
                continue
            if (xo, yo) == (x, y):
                continue
            #visited.remove((xo, yo)) if (xo, yo) in visited else None
            lines[xo][yo] += 1

def count_e(lines, visited):
    count = 0

    has_flash = True
    while has_flash:
        has_flash = False
        for i in range(len(lines)):
            for j in range(len(lines[i])):
                if lines[i][j] > 9 and (i, j) not in visited:
                    visited.add((i, j))
                    count += 1
                    #print('count', count)
                    has_flash = True
                    inc_adjacent(lines, i, j, visited)
    return count

def step(lines):
    for i in range(len(lines)):
        for j in range(len(lines[i])):
            lines[i][j] += 1

    count = count_e(lines, set())

    flash_count = 0
    for i in range(len(lines)):
        for j in range(len(lines[i])):
            if lines[i][j] > 9:
                lines[i][j] = 0
                flash_count += 1

    print('***')
    for i in range(len(lines)):
        print(lines[i])


    # part 2
    if flash_count == 100:
        print('done!')
        exit(0)
    # end part 2


    return count

if __name__=='__main__':
    lines = []
    for line in sys.stdin.readlines():
        lines.append(list(map(int, line.strip())))
    print('lines', lines)
    count = 0
    for i in range(1000000):
        print('--- i', i+1)
        count += step(lines)
    print('count', count)
