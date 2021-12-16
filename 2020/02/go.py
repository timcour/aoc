#!/usr/bin/env python3
# :22 - :35

import sys
from collections import Counter, defaultdict
from math import prod
from copy import deepcopy

def validate(rule, pw):
    c = Counter(pw)
    #return rule[1] <= c[rule[0]] <= rule[2]
    cnt = 0
    if rule[1] <= len(pw) and pw[rule[1]-1] == rule[0]:
        cnt += 1
    if rule[2] <= len(pw) and pw[rule[2]-1] == rule[0]:
        cnt += 1
    return cnt == 1

if __name__=='__main__':
    valid_count = 0
    for line in sys.stdin.readlines():
        r, pw = list(map(lambda x: x.strip(), line.strip().split(':')))
        r = r.replace('-', ' ')
        r = r.split(' ')
        rule = (r[2], int(r[0]), int(r[1]))
        print(rule, pw)
        if validate(rule, pw):
            valid_count += 1
    print(valid_count)
