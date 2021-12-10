#!/usr/bin/env python3

import sys
from collections import Counter
from math import prod

def in_bounds(data, x, y):
    if x < 0 or x >= len(data):
        return False
    if y < 0 or y >= len(data[0]):
        return False
    return True

def min_point(data, x, y):
    min_point = 10
    for i, j in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        if not in_bounds(data, x+i, y+j):
            continue
        if data[x+i][y+j] < min_point:
            min_point = data[x+i][y+j]

    if data[x][y] < min_point:
        return data[x][y]
    return None

def calc_risk_level(data):
    score = 0
    for i in range(len(data)):
        for j in range(len(data[i])):
            level = min_point(data, i, j)
            if level is not None:
                score += level + 1
    return score

def basin_size(data, x, y, visited):
    if not in_bounds(data, x, y):
        return 0
    if data[x][y] == 9:
        return 0

    if (x, y) in visited:
        return 0
    visited.add((x,y))

    count = 0
    for i, j in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        xo, yo = x+i, y+j
        count += basin_size(data, xo, yo, visited)
    return count + 1

def find_basins(data):
    mins = set()
    for i in range(len(data)):
        for j in range(len(data[i])):
            level = min_point(data, i, j)
            if level is not None:
                mins.add((i, j))

    basin_sizes = []
    visited = set()
    for m in mins:
        s = basin_size(data, m[0], m[1], visited)
        basin_sizes.append(s)

    return basin_sizes


if __name__=='__main__':
    data = []
    for line in sys.stdin.readlines():
        data.append(list(map(int, list(line.strip()))))
    print('data', data)
    # res = calc_risk_level(data)
    # print('result', res)
    res = find_basins(data)
    largest = sorted(res)[-3:]

    print('result', prod(largest))
