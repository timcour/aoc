#!/usr/bin/env python3

import sys
from collections import Counter, defaultdict
from math import prod
from copy import deepcopy

def find_insertions(tpl, rules):
    insertions = []
    # O(N)
    for i in range(1, len(tpl)):
        pair = tpl[i-1] + tpl[i]
        insertions.append((i, rules[pair]))
    return insertions

def step(tpl, rules):
    ins = find_insertions(tpl, rules)
    ins.reverse()
    bits = list(tpl)

    # O(N^2)
    for op in ins:
        bits.insert(op[0], op[1])
    return ''.join(bits)


def fast_step(tplmap, rules):
    ret = Counter()
    for k, v in rules.items():
        c = tplmap[k]
        a = k[0] + v
        b = v + k[1]
        ret[a] += c
        ret[b] += c
    return ret


def fast(tpl, rules, N):
    tplmap = Counter()
    for i in range(1, len(tpl)):
        pair = tpl[i-1] + tpl[i]
        tplmap[pair] += 1

    for i in range(N):
        tplmap = fast_step(tplmap, rules)

    cc = Counter([tpl[0], tpl[-1]])
    for k, v in tplmap.items():
        cc[k[0]] += v
        cc[k[1]] += v

    return int((max(cc.values()) - min(cc.values())) / 2)

def diff(tpl):
    c = Counter(tpl)
    return max(c.values()) - min(c.values())

if __name__=='__main__':
    tpl = sys.stdin.readline().strip()
    sys.stdin.readline() # empty line
    rules = {}

    for line in sys.stdin.readlines():
        pair, ic = line.strip().split(' -> ')
        rules[pair] = ic

    res = fast(tpl, rules, 40)
    print('result', res)
