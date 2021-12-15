#!/usr/bin/env python3
# :22 - :35

import sys
from collections import Counter, defaultdict
from math import prod
from copy import deepcopy
import heapq

def in_bounds(data, x, y):
    if x < 0 or x >= len(data):
        return False
    if y < 0 or y >= len(data[0]):
        return False
    return True

def get_neighbors(grid, node):
    nodes = []
    for ox, oy in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
        x = node[1][0] + ox
        y = node[1][1] + oy
        if in_bounds(grid, x, y):
            nodes.append((grid[x][y], (x, y)))
    return nodes

def find_shortest(grid):
    start = (0, 0)
    end = (len(grid[0])-1, len(grid)-1)

    shortest = defaultdict(lambda: 1e100)
    shortest[start] = 0
    nodes = [(0, start)]
    while nodes:
        #print('nodes', nodes)
        #print('shortest', shortest)
        node = heapq.heappop(nodes)
        neighbors = get_neighbors(grid, node)
        for neigh in neighbors:
            #print('neighbors', neighbors)
            curr = shortest[neigh[1]]
            new = neigh[0] + shortest[node[1]]
            if new < curr:
                shortest[neigh[1]] = new
                heapq.heappush(nodes, neigh)

    return shortest[end]



if __name__=='__main__':
    lines = []
    for line in sys.stdin.readlines():
        lines.append(list(map(int, list(line.strip()))))
    print(lines)
    short = find_shortest(lines)
    print('short', short)
