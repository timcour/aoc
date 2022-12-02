#!/usr/bin/env python3

import sys

WINS = set([
    ('A', 'C'),
    ('B', 'A'),
    ('C', 'B'),
])

WIN_MAP = dict(WINS)
LOSE_MAP = dict(map(reversed, WINS))

NORM = {
    'X': 'A',
    'Y': 'B',
    'Z': 'C',
}

def shape_points(s):
    return ord(s) - ord('A') + 1

def find_outcome(op, me):
    me = NORM[me]
    if (op == me):
        return 3
    if (me, op) in WINS:
        return 6
    return 0

def find_total_pt1(rounds):
    total = 0
    for r in rounds:
        total += find_outcome(*r) + shape_points(NORM[r[1]])
    return total

def find_shape(opponent, outcome):
    if outcome == 'Z': # Lose
        return LOSE_MAP[opponent]
    if outcome == 'Y': # Draw
        return opponent
    if outcome == 'X': # Win
        return WIN_MAP[opponent]

def find_total(rounds):
    total = 0
    for r in rounds:
        desired_shape = find_shape(*r)
        total += shape_points(desired_shape)
        total += (ord(r[1]) - ord('X')) * 3
        # print('round', r, 'outcome points', (ord(r[1]) - ord('X')) * 3,
        #       'shape points:', shape_points(desired_shape), 'desired_shape:', desired_shape)
    return total

if __name__=='__main__':
    lines = []
    for line in sys.stdin.readlines():
        lines.append(line.split())

    print('pt1-total', find_total_pt1(lines))
    print('pt2-total', find_total(lines))
