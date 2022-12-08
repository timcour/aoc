#!/usr/bin/env python3

import sys

def find_visible_in_line(grid, hor, ver):
    vis = set()
    count = 0
    last = -1
    for i in range(*ver):
        for j in range(*hor):
            if grid[i][j] > last:
                vis.add((i, j))
            last = max([last, grid[i][j]])
            count +=1
    return vis

def find_visible(grid):
    vis = set()
    lr = [0, len(grid[0])]
    rl = [len(grid[0]) -1, -1, -1]
    ud = [0, len(grid)]
    du = [len(grid) -1, -1, -1]

    for i in range(len(grid)):
        r = find_visible_in_line(grid, [i, i + 1], lr)
        vis = vis.union(r)
        r = find_visible_in_line(grid, [len(grid) - i - 1, len(grid) - i], rl)
        vis = vis.union(r)
    for i in range(len(grid[0])):
        r = find_visible_in_line(grid, ud, [i, i + 1])
        vis = vis.union(r)
        r = find_visible_in_line(grid, du, [len(grid[0]) - i - 1, len(grid[0]) - i])
        vis = vis.union(r)

    return vis

def find_view(grid, coord, d):
    x0, y0 = coord[0], coord[1]
    h = grid[coord[0]][coord[1]]

    count = 0
    x, y = x0, y0

    while True:
        x += d[0]
        y += d[1]
        if x < 0 or x >= len(grid) or y < 0 or y >= len(grid[0]):
            return count
        count += 1
        if grid[x][y] >= grid[x0][y0]:
            return count
    return count

def find_score(grid):
    dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    scores = []
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            score = 1
            for d in dirs:
                score *= find_view(grid, (i, j), d)
            scores.append(score)
    return max(scores)

if __name__=='__main__':
    grid = []
    for line in sys.stdin.readlines():
        parts = list(map(int, list(line.strip())))
        grid.append(parts)

    vis = find_visible(grid)
    print('pt-1:', len(vis))
    score = find_score(grid)
    print('pt-2:', score)
