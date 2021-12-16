#!/usr/bin/env python3

import sys
from collections import Counter, defaultdict
from math import prod
from copy import deepcopy
import heapq
from numpy import concatenate as concat

def in_bounds(data, x, y, mul=5):
    if x < 0 or x >= len(data) * mul:
        return False
    if y < 0 or y >= len(data[0]) * mul:
        return False
    return True

def node_at(grid, x, y):
    xroot = x % len(grid)
    yroot = y % len(grid[0])
    root_val = grid[xroot][yroot]
    xo, yo = x // len(grid), y // len(grid[0])
    val = (root_val + xo + yo - 1) % 9 + 1
    return (val, (x, y))

def get_neighbors(grid, node, mul=5):
    nodes = []
    for ox, oy in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
        x = node[1][0] + ox
        y = node[1][1] + oy
        if in_bounds(grid, x, y, mul=mul):
            neighbor = node_at(grid, x, y)
            nodes.append(neighbor)

    return nodes

def find_shortest(grid, mul=5):
    start = (0, 0)
    end = (len(grid[0]) * mul - 1, len(grid) * mul - 1)

    shortest = defaultdict(lambda: 1e100)
    shortest[start] = 0
    nodes = [(0, start)]

    visited = set()
    while nodes:
        node = heapq.heappop(nodes)
        visited.add(node[1])
        if node[1] == end:
            return node[0] # minor optimization in this case

        neighbors = get_neighbors(grid, node, mul=mul)
        # filter saves about 1/2 the iters
        for neigh in filter(lambda n: n[1] not in visited, neighbors):
            curr = shortest[neigh[1]]
            new = neigh[0] + shortest[node[1]]
            if new < curr:
                shortest[neigh[1]] = new
                neigh = (new, neigh[1])
                heapq.heappush(nodes, neigh)

    return shortest[end]

def printem(grid):
    for i in range(len(grid) * 5):
        for j in range(len(grid[0]) * 5):
            node = node_at(grid, i, j)
            print(node[0], end='')
        print()

if __name__=='__main__':
    lines = []
    for line in sys.stdin.readlines():
        lines.append(list(map(int, list(line.strip()))))

    MUL = 5
    print('node count', len(concat(lines)) * MUL**2)
    short = find_shortest(lines, mul=MUL)
    print('short', short)
