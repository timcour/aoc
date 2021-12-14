#!/usr/bin/env python3

import sys
from collections import Counter, defaultdict
from math import prod
from copy import deepcopy



def is_small(node):
    if node in ['start', 'end']:
        return False
    return 'a' <= node[0] <= 'z'

def add_edge(graph, a, b):
    if a == 'start':
        graph[a].append(b)
    elif b == 'end':
        graph[a].append(b)
    else:
        graph[a].append(b)
        graph[b].append(a)


def _find_paths(graph, a, curr, twosmall=False, lst=None):
    if a == 'end':
        lst.append('end')
        print('path', '-'.join(lst))
        return 1
    if a in curr and is_small(a):
        if twosmall:
            return 0
        twosmall = True
    curr.add(a)
    lst.append(a)
    count = 0
    for b in graph[a]:
        count += _find_paths(graph, b, curr.copy(), twosmall, lst.copy())
    return count

def find_paths(graph):
    start = graph['start']
    return _find_paths(graph, 'start', set(), False, [])

if __name__=='__main__':
    graph = defaultdict(list)
    for line in sys.stdin.readlines():
        a, b = line.strip().split('-')
        if a == 'end' or b == 'start':
            a, b = b, a
        add_edge(graph, a, b)

    print('graph', graph)
    paths = find_paths(graph)
    print('paths', paths)
