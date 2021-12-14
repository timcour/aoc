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

# Returns the stack and first mismatched token if corrupt
def parse(tokens):
    stack = []
    for t in tokens:
        if t in openers:
            stack.append(t)
            continue
        if M[t]['o'] == stack[-1]:
            stack.pop()
        else:
            return stack, t
    return stack, None

def find_score(tokens):
    stack, t = parse(tokens)
    return M[t]['score'] if t else 0

def completion_score(tokens):
    stack, t = parse(tokens)
    score = 0
    while stack:
        o = stack.pop()
        c = O2C[o]
        score = score * 5 + M[c]['s2']
    return score

def find_winner(lines):
    lines = filter(lambda x: find_score(x) == 0, lines)
    scores = []
    for line in lines:
        s = completion_score(line)
        scores.append(s)
    return sorted(scores)[int(len(scores) / 2)]

def find_corrupt_score(lines):
    total = 0
    for line in lines:
        s = find_score(line)
        total += s
    return total

if __name__=='__main__':
    lines = []
    for line in sys.stdin.readlines():
        lines.append(list(line.strip()))
    total = find_corrupt_score(lines)
    print('corrupt score:', total)
    res = find_winner(lines)
    print('autocomplete score:', res)
