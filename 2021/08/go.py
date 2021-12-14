#!/usr/bin/env python3

import sys
from collections import Counter

def get_counts(pat):
    counts = Counter()
    for p in pat:
        chars = list(p)
        counts += Counter(chars)
    return counts

freq_mapping = {
    (4, 6, 7, 7, 8, 8, 9): 8,
    (6, 7, 7, 8, 9): 5,
    (4, 7, 7, 8, 8): 2,
    (7, 7, 8, 8, 9): 3,
    (8, 8, 9): 7,
    (6, 7, 7, 8, 8, 9): 9,
    (4, 6, 7, 7, 8, 9): 6,
    (6, 7, 8, 9): 4,
    (4, 6, 7, 8, 8, 9): 0,
    (8, 9): 1,
}

def get_digit(out, counts):
    oc = Counter(out)
    for pc in oc:
        oc[pc] = counts[pc]
    key = tuple(sorted(oc.values()))
    ans = freq_mapping[key]
    return ans

def find_reading(pat, out):
    counts = get_counts(pat)
    s = ''
    for p in out:
        s += str(get_digit(p, counts))
    return int(s)

if __name__=='__main__':
    data = []
    for line in  sys.stdin.readlines():
        pat, out = line.split('|')
        data.append({'pat': pat.split(), 'out': out.split()})

    readings = []

    for d in data:
        reading = find_reading(d['pat'], d['out'])
        print('reading', reading)
        readings.append(reading)

    print('Total:', sum(readings))
