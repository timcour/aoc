#!/usr/bin/env python3
# :46 - :53

import sys
from collections import Counter, defaultdict
from math import prod
from copy import deepcopy


# General (N numbers in nums that sum to target)
def find_sum(nums, target, N, curr):
    if N == 0:
        return curr if sum(curr) == target else None

    for i, v in enumerate(nums):
        r = find_sum(nums[i+1:], target, N-1, curr + [v])
        if r:
            return r

    return None

# Special (3 numbers in nums that sum to 2020)
def find_2020(nums):
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            for k in range(j+1, len(nums)):
                if nums[i] + nums[j] + nums[k] == 2020:
                    return nums[i], nums[j], nums[k]
    return None


if __name__=='__main__':
    nums = []
    for line in sys.stdin.readlines():
        nums.append(int(line.strip()))

    #res = find_2020(nums)

    target = 2020
    res = find_sum(nums, target, 3, [])
    if not res:
        print("Error: failed to find target", target)
        exit(-1)
    pres = prod(res)
    print(pres)
    assert pres == 66432240, 'Unexpected product'
