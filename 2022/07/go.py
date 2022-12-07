#!/usr/bin/env python3

import sys
import parse
from pprint import pprint
from collections import defaultdict as dd
from bisect import bisect_right

def add(tree, path, target):
    curr = tree
    for seg in path:
        curr = curr[seg]

    if target['type'] == 'dir':
        if target['key'] in curr:
            return
        curr[target['key']] = {}
    elif target['type'] == 'file':
        curr[target['key']] = target
    else:
        raise ('unknown target', target)

def find_dir_size(tree, path, sizes):
    size = 0
    for k in tree.keys():
        if tree[k].get('type') == 'file':
            size += tree[k]['size']
        else:
            p = path.copy()
            p.append(k)
            s = find_dir_size(tree[k], p, sizes)
            size += s
    sizes['/'.join(path)] = size
    return size

def find_size_sum(sizes):
    total = 0
    for k in sizes:
        if sizes[k] <= 100000:
            total += sizes[k]
    return total

def find_gt(a, x):
    'Find leftmost value greater than x'
    i = bisect_right(a, x)
    if i != len(a):
        return a[i]
    raise ValueError

def find_dir_for_delete(tree):
    size_req = 30000000
    total_fs = 70000000
    sizes = {}
    curr_used = find_dir_size(tree, [], sizes)
    needed = size_req - (total_fs - curr_used)
    sorted_sizes = sorted(list(sizes.values()))
    result = find_gt(sorted_sizes, needed)
    return result

if __name__=='__main__':
    tree = {'/': {}}
    path = []
    for line in sys.stdin.readlines():
        parts = line.split()
        if parts[0] == '$':
            if parts[1] == 'ls':
                # print('ls', parts)
                pass
            elif parts[1] == 'cd':
                if parts[2] == '..':
                    path.pop()
                else:
                    path.append(parts[2])
        elif parts[0] == 'dir':
            t = {'key': parts[1], 'type': 'dir'}
            add(tree, path, t)
        else:
            t = {'key': parts[1], 'type': 'file', 'size': int(parts[0])}
            add(tree, path, t)

    # pprint(tree)
    sizes = {}
    size = find_dir_size(tree, [], sizes)
    print('pt-1:', find_size_sum(sizes))

    result = find_dir_for_delete(tree)
    print('pt-2:', result)
