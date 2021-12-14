#!/usr/bin/env python3
# :46 - :53

import sys
from collections import Counter, defaultdict
from math import prod
from copy import deepcopy


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
    pair = find_2020(nums)
    r = pair[0] * pair[1] * pair[2]
    print('r', r)
