#!/usr/bin/env python3

import sys
from collections import Counter
from math import prod

M = {
    ')': {'o': '(', 'score': 3,     's2': 1},
    ']': {'o': '[', 'score': 57,    's2': 2},
    '}': {'o': '{', 'score': 1197,  's2': 3},
    '>': {'o': '<', 'score': 25137, 's2': 4}
}

openers = set(map(lambda m: m['o'], M.values()))
O2C = {}
for k in M:
    O2C[M[k]['o']] = k


def find_score(tokens):
    stack = []
    for t in tokens:
        if t in openers:
            stack.append(t)
            continue
        if M[t]['o'] == stack[-1]:
            stack.pop()
        else:
            return M[t]['score']
    return 0

def is_corrupt(tokens):
    stack = []
    for t in tokens:
        if t in openers:
            stack.append(t)
            continue
        if M[t]['o'] == stack[-1]:
            stack.pop()
        else:
            return True
    return False

def completion_score(tokens):
    stack = []
    for t in tokens:
        if t in openers:
            stack.append(t)
            continue
        if M[t]['o'] == stack[-1]:
            stack.pop()

    score = 0
    while stack:
        o = stack.pop()
        c = O2C[o]
        score = score * 5 + M[c]['s2']
    return score

def find_winner(lines):
    lines = filter(lambda x: not is_corrupt(x), lines)

    scores = []
    for line in lines:
        s = completion_score(line)
        scores.append(s)
        print('score', s)

    return sorted(scores)[int(len(scores) / 2)]

if __name__=='__main__':
    lines = []
    for line in sys.stdin.readlines():
        lines.append(list(line.strip()))
    print('lines', lines)
    # total = 0
    # for line in lines:
    #     s = find_score(line)
    #     total += s
    #     print('score', s)
    # print('total', total)
    res = find_winner(lines)
    print('res', res)
