#!/usr/bin/env python3

import sys

def find_max(counts):
    totals = []
    for count in counts:
        totals.append(sum(count))
    return max(totals)

def top_n(counts, n):
    totals = []
    for count in counts:
        totals.append(sum(count))
    totals.sort()
    return totals[-n:]

if __name__=='__main__':
    counts = [[]]
    for line in sys.stdin.readlines():
        if line.strip() == '':
            counts.append([])
        else:
            counts[-1].append(int(line.strip()))

    print(find_max(counts))

    print('top three', sum(top_n(counts, 3)))
