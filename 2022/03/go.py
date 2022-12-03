#!/usr/bin/env python3

import sys

def find_prio(n):
    if ord(n) < ord('a'):
        return ord(n) - ord('A') + 27
    return ord(n) - ord('a') + 1

def find_intersect(*chars):
    scratch = set(chars[0])
    for i in range(int(len(chars))):
        scratch = scratch.intersection(set(chars[i]))

    return list(scratch)[0]

if __name__=='__main__':
    lines = []

    for line in sys.stdin.readlines():
        line = list(line.strip())
        lines.append(line)

    prios = []
    for line in lines:
        n = int(len(line)/2)
        a = set(line[:n])
        b = set(line[n:])
        c = find_intersect(a, b)

        prio = find_prio(c)
        prios.append(prio)

    print('prios-1', sum(prios))

    prios = []
    for i in range(int(len(lines)/3)):
        prio = find_prio(find_intersect(lines[i*3], lines[i*3+1], lines[i*3+2]))
        prios.append(prio)

    print('prios-2', sum(prios))
