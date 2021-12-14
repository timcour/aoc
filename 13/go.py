#!/usr/bin/env python3

# :25

import sys
from collections import Counter, defaultdict
from math import prod
from copy import deepcopy



def foldit(coords, inst):
    d, i = inst

    trash = set()
    new = set()
    for c in coords:
        if d == 'x' and c[0] > i:
            x = 2*i - c[0]
            new.add((x, c[1]))
            trash.add(c)
        if d == 'y' and c[1] > i:
            y = 2*i - c[1]
            new.add((c[0], y))
            trash.add(c)

    coords = coords - trash
    coords = coords.union(new)
    return coords

def pprint(coords):
    get_nums = lambda i: map(lambda x: x[i], coords)
    minx, maxx = min(get_nums(0)), max(get_nums(0))
    miny, maxy = min(get_nums(1)), max(get_nums(1))
    for i in range(miny, maxy+1):
        for j in range(minx, maxx+1):
            if (j, i) in coords:
                print('#', end='')
            else:
                print('.', end='')
        print('')

if __name__=='__main__':
    coords = set()
    folds = []
    for line in sys.stdin.readlines():
        if (line.startswith('fold along')):
            fold = line.strip('fold along ').split('=')
            fold[1] = int(fold[1])
            folds.append(fold)
        elif line == '\n':
            continue
        else:
            coord = tuple(map(int, line.strip().split(',')))
            coords.add(coord)

    print('folds', folds)
    for i in range(len(folds)):
        f = folds[i]
        coords = foldit(coords, f)
        print('len coords', len(coords))
    pprint(coords)
