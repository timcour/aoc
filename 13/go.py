#!/usr/bin/env python3

# :25

import sys
from collections import Counter, defaultdict
from math import prod
from copy import deepcopy



def foldit(coords, inst):
    d, i = inst
    thresh = (0, 0)
    if inst[0] == 'x':
        thresh = (inst[1], 0)
    else:
        thresh = (0, inst[1])

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
    minx, maxx = min(map(lambda x: x[0], coords)), max(map(lambda x: x[0], coords))
    miny, maxy = min(map(lambda x: x[1], coords)), max(map(lambda x: x[1], coords))
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
            print('fold', line)
            fold = line.strip('fold along ').split('=')
            fold[1] = int(fold[1])
            folds.append(fold)

        elif line == '\n':
            continue
        else:
            coord = tuple(map(int, line.strip().split(',')))
            coords.add(coord)

    print('coords', coords)
    pprint(coords)


    print('folds', folds)
    for i in range(len(folds)):
        f = folds[i]
        print('i', i, 'fold', f)

        coords = foldit(coords, f)
        print('coords', coords)
        print('len coords', len(coords))
        pprint(coords)
