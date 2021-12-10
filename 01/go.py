#!/usr/bin/env python3

import sys

def count_incs(nums):
    last = nums[0]
    count = 0
    for num in nums:
        if num > last:
            count += 1
        last = num
    return count

class Agg:
    def __init__(self):
        self.window = [0, 0, 0]
        self.i = 0

    def add(self, num):
        self.window[self.i] = num
        self.i = (self.i + 1) % len(self.window)

def count_win_incs(nums):
    count = 0
    a = Agg()
    b = Agg()
    for i in range(0, len(nums)):
        n = nums[i]
        a.add(n)
        if sum(a.window) > sum(b.window) and i >= len(a.window):
            count += 1
        b.add(n)
    return count

if __name__=='__main__':
    lines = []
    for line in sys.stdin.readlines():
        lines.append(int(line))

    res = count_win_incs(lines)
    print(res)
