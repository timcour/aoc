#!/usr/bin/env python3

import sys


def doit(lines):
    depth = 0
    pos = 0
    aim = 0
    for line in lines:
        if line[0] == 'forward':
            pos += line[1]
            depth += aim * line[1]
        elif line[0] == 'down':
            aim += line[1]
        elif line[0] == 'up':
            aim -= line[1]
        else:
            print('whats', line[0])
    return depth * pos

if __name__=='__main__':
    lines = []
    for line in sys.stdin.readlines():
        parts = line.split(' ')
        lines.append((parts[0], int(parts[1])))
    res = doit(lines)
    print('res', res)
