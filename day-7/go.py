#!/usr/bin/env python3

import sys
from collections import Counter

def calc_fuel_1(positions, dest):
    return sum(map(lambda x: abs(x - dest), positions))

def calc_fuel(positions, dest):
    return sum(map(lambda x: abs(x - dest) * (abs(x - dest) +1)/2, positions))

def find_min(pos):
    pos.sort()
    print(pos)
    ave = sum(pos) / len(pos)
    print('ave', ave)

    maxp = max(pos)
    minp = min(pos)

    minf = None
    for i in range(minp, maxp+1):
        f = calc_fuel(pos, i)
        print('f', f)
        if minf == None or f < minf:
            minf = f

    return minf

if __name__=='__main__':
    positions = list(map(int, sys.stdin.readline().split(',')))
    res = find_min(positions)
    print('result', res)
