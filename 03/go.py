#!/usr/bin/env python3

import sys
import copy

def ge(lines, mul=1):
    print('lines', lines)
    g = ''
    for i in range(len(lines[0])):
        occ = map(lambda l: int(l[i]), lines)
        occ = list(occ)
        print('occ', list(occ))
        print('sum', sum(occ))
        if sum(occ) > len(lines) / 2.:
            g += '1' if mul == 1 else '0'
        else:
            g += '0' if mul == 1 else '1'
    return g

# ox gen rating - most common. if equal, keep 1.
# co2 scrubber rating. least common. if equal, keep 0.

def find_common(lines, i):
    occ = map(lambda l: int(l[i]), lines)
    occ = list(occ)
    print('---')
    print('i', i)
    print('len lines', len(lines))
    print('sum(occ)', sum(occ))
    if sum(occ) > len(lines) / 2:
        print('1')
        return 1
    if sum(occ) < len(lines) / 2:
        print('-1')
        return -1
    print('0')
    return 0

def life(lines):
    print('lines', lines)
    res = copy.copy(lines)
    i = 0
    while len(res) > 1:
        check = '1' if find_common(res, i) in [1, 0] else '0'
        res = list(filter(lambda l: l[i] == check, res))
        print('res tmp', res)
        i += 1
    return ''.join(res[0])

# oldie but goodie, why factor when you can copy pasta!!!
def life2(lines):
    print('lines', lines)
    res = copy.copy(lines)
    i = 0
    while len(res) > 1:
        check = '1' if find_common(res, i) in [-1] else '0'
        print('check', check)
        res = list(filter(lambda l: l[i] == check, res))
        print('res tmp', res)
        i += 1
    return ''.join(res[0])


if __name__=='__main__':
    lines = []
    for line in sys.stdin.readlines():
        print('appending', line)
        lines.append(list(line.strip()))

    ox = life(lines)
    print('ox', ox)
    co2 = life2(lines)
    print('co2', co2)
    res = int(ox, 2) * int(co2, 2)
    print('res', res)
