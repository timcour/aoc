#!/usr/bin/env python3

import sys
from collections import defaultdict

def mark_line(start, end, marks):
    # if start[0] != end[0] and start[1] != end[1]:
    #     print('diag... skipping', start, end)
    #     return marks

    xd = (start[0] < end[0]) - (start[0] > end[0])
    yd = (start[1] < end[1]) - (start[1] > end[1])

    xs, xe = start[0], end[0]
    ys, ye = start[1], end[1]

    diff = max(map(abs, [start[0] - end[0], start[1] - end[1]]))
    x, y = xs, ys
    for _ in range(diff+1):
        marks[(x, y)] += 1
        x += xd
        y += yd


def mark_pairs(pairs):
    marks = defaultdict(int)
    for pair in pairs:
        mark_line(pair[0], pair[1], marks)

    count = 0
    for v in marks.values():
        if v > 1:
            count += 1

    return count


if __name__=='__main__':
    pairs = []
    for line in sys.stdin.readlines():
        a, b = map(lambda x: tuple(map(int, x.split(','))), line.split(' -> '))
        pairs.append((a, b))

    res = mark_pairs(pairs)
    print('result:', res)
