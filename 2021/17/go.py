#!/usr/bin/env python3

import sys
from collections import Counter, defaultdict
from math import prod
from copy import deepcopy
import heapq
import json
import parse

class Target:
    def __init__(self, xmin, xmax, ymin, ymax):
        self.xmin = xmin
        self.xmax = xmax
        self.ymin = ymin
        self.ymax = ymax
    def contains(self, point):
        return (
            self.xmin <= point[0] <= self.xmax
            and self.ymin <= point[1] <= self.ymax
        )
    def missed(self, point):
        return (self.ymin > point[1] or self.xmax < point[0])


# p - current point, v - velocity
# return (new point, new velocity)
def step(p, v):
    p2 = (p[0] + v[0], p[1] + v[1])
    mul = -1 if v[0] < 0 else 1
    v2x = mul * max(abs(v[0]) - 1, 0)
    v2 = (v2x, v[1]-1)
    return (p2, v2)


def find_max_y(target):
    max_y, hits = 0, []
    for i in range(5, 51):
        for j in range(-300, 300):
            p, v, tmp_y = (0, 0), (i, j), 0
            while True:
                p, v = step(p, v)
                tmp_y = max(tmp_y, p[1])
                if target.missed(p):
                    break
                if target.contains(p):
                    hits.append((i, j))
                    max_y = max(tmp_y, max_y)
                    break
    return max_y, hits


if __name__=='__main__':
    xmin, xmax, ymin, ymax = parse.parse(
        'target area: x={:d}..{:d}, y={:d}..{:d}',
        sys.stdin.readline().strip()
    )
    target = Target(xmin, xmax, ymin, ymax)
    y, hits = find_max_y(target)
    print('y', y)
    print('hits', len(hits))


def test_step():
    p, v = (0, 0), (-1, 2)
    p, v = step(p, v)
    assert p == (-1, 2)
    assert v == (0, 1)
    p, v = step(p, v)
    assert p == (-1, 3)
    assert v == (0, 0)

def test_contains():
    target = Target(1, 5, 2, 6)
    assert target.contains((2, 3))
    assert target.contains((5, 6))
    assert not target.contains((2, 7))
