#!/usr/bin/env python3

import sys
from parse import *

#     [H]         [D]     [P]
# [W] [B]         [C] [Z] [D]
# [T] [J]     [T] [J] [D] [J]
# [H] [Z]     [H] [H] [W] [S]     [M]
# [P] [F] [R] [P] [Z] [F] [W]     [F]
# [J] [V] [T] [N] [F] [G] [Z] [S] [S]
# [C] [R] [P] [S] [V] [M] [V] [D] [Z]
# [F] [G] [H] [Z] [N] [P] [M] [N] [D]
#  1   2   3   4   5   6   7   8   9

# input transformed by hand
stacks = [
    ['F', 'C', 'J', 'P', 'H', 'T', 'W'],
    ['G', 'R', 'V', 'F', 'Z', 'J', 'B', 'H'],
    ['H', 'P', 'T', 'R'],
    ['Z', 'S', 'N', 'P', 'H', 'T'],
    ['N', 'V', 'F', 'Z', 'H', 'J', 'C', 'D'],
    ['P', 'M', 'G', 'F', 'W', 'D', 'Z'],
    ['M', 'V', 'Z', 'W', 'S', 'J', 'D', 'P'],
    ['N', 'D', 'S'],
    ['D', 'Z', 'S', 'F', 'M'],
]

def move(stacks, frm, to, count):
    for i in range(count):
        stacks[to].append(stacks[frm].pop())

def move_rev(stacks, frm, to, count):
    buff = []
    for i in range(count):
        buff.append(stacks[frm].pop())
    while buff:
        stacks[to].append(buff.pop())

def print_top(stacks):
    for stack in stacks:
        print(stack[-1], end='')
    print()

if __name__=='__main__':
    print('stacks', stacks)
    cmds = []
    for line in sys.stdin.readlines():
        count, f, t = parse('move {} from {} to {}', line.strip())
        cmds.append((int(f)-1, int(t)-1, int(count)))

    for cmd in cmds:
        move(stacks, *cmd)
        move_rev(stacks, *cmd)

    print_top(stacks)
