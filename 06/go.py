#!/usr/bin/env python3

import sys
from collections import Counter

def next_gen(state):
    c = Counter()
    for k in state:
        if k == 0:
            c[8] += state[k]
            c[6] += state[k]
        else:
            c[k-1] += state[k]
    return c

if __name__=='__main__':
    istate = list(map(int, sys.stdin.readline().split(',')))
    print('istate', istate)
    state = Counter(istate)
    for i in range(256):
        state = next_gen(state)
    print('result:', sum(state.values()))
