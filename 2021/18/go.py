#!/usr/bin/env python3

import sys
from collections import Counter, defaultdict
from math import prod
from copy import deepcopy
import heapq
import json
import parse

# I bet there's some lib that does this.
def setv(tree, path, fn):
    node = tree
    for i in range(len(path) - 1):
        node = node[path[i]]
    node[path[-1]] = fn(node[path[-1]])

def getv(tree, path):
    node = tree
    for i in range(len(path)):
        node = node[path[i]]
    return node

def find_ordered_paths(tree, path, paths):
    for i in range(len(tree)):
        curr = path + (i,)
        if type(tree[i]) == int:
            paths.append(curr)
            continue
        find_ordered_paths(tree[i], curr, paths)
    return paths

# DFS, visit every number in order
# Keep track of ordered paths
# Find first path w/ len 5 (pair is at depth 4)
# update path before and second path after, then set the pair to 0.
# return True if explode happened, False otherwise
def explode(tree):
    ordered_paths = find_ordered_paths(tree, (), [])
    for i in range(len(ordered_paths)):
        path = ordered_paths[i]
        if len(path) == 5:
            snailpath = path[:-1]
            snailnum = getv(tree, snailpath)
            if i > 0:
                setv(tree, ordered_paths[i-1], lambda v: v+snailnum[0])
            if i < len(ordered_paths) - 2:
                # the very next path is the second part of snailnum
                setv(tree, ordered_paths[i+2], lambda v: v+snailnum[1])
            setv(tree, snailpath, lambda v: 0)
            return True
    return False

def split(tree):
    for i in range(len(tree)):
        val = tree[i]
        if type(val) == int:
            if val > 9:
                tree[i] = [val // 2, -(val // -2)]
                return True
        else:
            if split(val):
                return True
    return False

def add(a, b):
    r = [a, b]
    while explode(r) or split(r):
        pass
    return r

def is_pair(tree):
    if type(tree) != list:
        return False
    if len(tree) != 2:
        return False
    return sum(map(lambda x: type(x) == int, tree)) == 2

def magnitude(tree, depth=0):
    if type(tree) == int:
        return tree
    if is_pair(tree):
        return 3*tree[0] + 2*tree[1]
    for i in range(len(tree)):
        while type(tree[i]) != int:
            tree[i] = magnitude(tree[i], depth+1)
    return magnitude(tree)

def find_max_sum(nums):
    mmax = 0
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            for k in range(2):
                t = [deepcopy(nums[i]), deepcopy(nums[j])]
                t[0+k], t[(1+k) % 2] = t[0], t[1]
                s = add(t[0], t[1])
                m = magnitude(s)
                if m > mmax:
                    mmax = m
            print('\r%s, %s, max: %s' % (i, j, mmax), end='\r')

    print()
    return mmax


if __name__=='__main__':
    nums = []
    for line in  sys.stdin.readlines():
        nums.append(json.loads(line.strip()))

    r = find_max_sum(nums)
    print('max sum', r)

    acc = nums[0]
    for num in nums[1:]:
        acc = add(acc, num)
    mag = magnitude(acc)
    print('pt. 1 mag', mag)
