#!/usr/bin/env python3

import sys

def find_overlap(a, b):
    last = 0
    overlap = 0
    count = 0

    starts = sorted([a[0], b[0]], reverse=True)
    ends = sorted([a[1], b[1]], reverse=True)
    while ends:
        if not starts or ends[-1] < starts[-1]:
            end = ends.pop()
            if count == 2:
                overlap += end - last + 1
            count -= 1
            last = end
        else:
            start = starts.pop()
            count += 1
            last = start

    return overlap

def full_overlap(a, b):
    overlap = find_overlap(a, b)
    return overlap in [a[1] - a[0] + 1, b[1] - b[0] + 1]

if __name__=='__main__':
    pairs = []
    for line in sys.stdin.readlines():
        pair = list(map(lambda p: tuple(map(int, p.split('-'))), line.split(',')))
        pairs.append(pair)

    count = 0
    for pair in pairs:
        if full_overlap(pair[0], pair[1]):
            count += 1
    print('pt-1:', count)

    count = 0
    for pair in pairs:
        if find_overlap(pair[0], pair[1]) > 0:
            count += 1
    print('pt-2:', count)
