#!/usr/bin/env python3

# 1 - 2 seg
# 4 - 4 seg
# 7 - 3 seg
# 8 - 7 seg

import sys
from collections import Counter

# 2 - not 3 or 5
# 3 - one char from each of the other five seg nums
# 5 - both chars in each of the 6 seg nums
# 6 - both from 5, one from 2
# 9 - set of chars from 3 and 5
# 0 - single unique missing char

uniques = set([2, 4, 3, 7])

def find_uniques(data):
    count = 0
    for d in data:
        for o in d['out']:
            if len(o) in uniques:
                count += 1
    return count



def get_counts(pat):
    counts = Counter()
    for p in pat:
        chars = list(p)
        counts += Counter(chars)
    return counts

def find_missing(pat, counts, n, pred):
    keys = list(counts.keys())
    vals = list(counts.values())
    print('counts', counts, n)
    i = vals.index(n)
    c = keys[i]
    for p in pat:
        if pred(pat, c):
            return p
    return None

def find_mapping(pat):
    mapping = {}

    counts = Counter()
    pat = set(filter(lambda p: len(p) in [5, 6], pat))
    # 0
    counts = get_counts(pat)
    zero = find_missing(pat, counts, 5, lambda pat, c: c not in pat)
    mapping[zero] = 0
    pat.remove(zero)

    # 2
    counts = get_counts(pat)
    two = find_missing(pat, counts, 4, lambda pat, c: c not in pat)
    mapping[two] = 2
    pat.remove(two)

    # 3
    counts = get_counts(pat)
    three = find_missing(pat, counts, 3, lambda pat, c: c not in pat)
    mapping[three] = 3

    print('pat', pat)
    print('counts', counts)
    print('mapping', mapping)

    # 6
    six = find_missing(pat, counts, 1, lambda pat, c: c in pat)
    mapping[six] = 6
    pat.remove(three)
    pat.remove(six)

    for p in pat:
        if len(p) == 5:
            mapping[p] = 5
        else:
            mapping[p] = 9

    print('mapping', mapping)


if __name__=='__main__':
    data = []
    for line in  sys.stdin.readlines():
        pat, out = line.split('|')
        data.append({'pat': pat.split(), 'out': out.split()})
    print(data)

    find_mapping(['acedgfb', 'cdfbe', 'gcdfa', 'fbcad', 'dab', 'cefabd', 'cdfgeb', 'eafb', 'cagedb', 'ab'])

    #result = find_uniques(data)
    #print('result:', result)
