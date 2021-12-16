#!/usr/bin/env python3

import sys
from collections import Counter, defaultdict
from math import prod
from copy import deepcopy
import heapq
from numpy import concatenate as concat
import json


# first 3 bits - packet ""version""
# next 3 - type ID

# 4 - literal value
# groups start w/ 1 until the last which starts w/ 0

# operator (non 4)
# mode - bit following header (7)
#  mode 0 - next 15 bits - total length in bits of sub-packets
# 1 next 11 bits number of sub-packets immediately contained


def readn(bits, s, n):

    # find char index start, end
    i = s // 4
    j = -((s + n) // -4)

    # find bitmask
    bi = s % 4
    bj = (4 - (s + n)) % 4

    mask = int('F' * (j - i), 16)
    mask = mask >> bi >> bj
    mask = mask << bj

    # find the inclusive hex chars
    h = bits[i:j]
    hi = int(bits[i:j], 16)

    return (mask & hi) >> bj

def test_readn():
    s = 'ABC'
    r = readn(s, 0, 1)
    assert r == 1
    r = readn(s, 1, 3)
    assert r == 2
    r = readn(s, 7, 3)
    assert r == 7
    r = readn(s, 8, 4)
    assert r == 12
    s = 'ABCDEFG'
    r = readn(s, 3, 15)
    print('r', r)
    print('data', f'{r:0x}')

def read_literal(bits, start, version, typeid):
    go = 1
    nums = []
    while go == 1:
        go = readn(bits, start, 1)
        n = readn(bits, start+1, 4)
        nums.append(n)
        start += 5

    total = 0
    for i, num in enumerate(nums):
        total += nums[i] * 16 ** (len(nums) - 1 - i)

    packet = {
        "type": typeid,
        "version": version,
        "value": total
    }

    return (start, packet)

def parse_op(bits, i, version, typeid):
    packet = {
        "type": typeid,
        "version": version
    }

    mode = readn(bits, i, 1)
    i += 1
    numbits = 0
    if mode == 0:
        # number of sub packets
        numbits = 15
        bitlen = readn(bits, i, numbits)
        i += numbits

        # this is wrong since the bit alignment is off
        # datanum = readn(bits, i, bitlen)
        # data = f'{datanum:0x}'
        # packets = parse(data)

        # instead, just process packets directly
        packets = []
        end = i + bitlen
        while i < end:
            i, p = parse_packet(bits, i)
            packets.append(p)

        packet['packets'] = packets
        return (i, packet)

    # number of bits of subpackets
    numbits = 11
    numpackets = readn(bits, i, numbits)
    i += numbits
    packets = []
    for _ in range(numpackets):
        i, pak = parse_packet(bits, i)
        packets.append(pak)
    packet['packets'] = packets
    return i, packet

def parse_packet(bits, i):

    if len(bits) * 4 - 11 < i:
        return i, None

    version = readn(bits, i, 3)
    typeid = readn(bits, i+3, 3)
    if typeid == 4:
        i, packet = read_literal(bits, i + 6, version, typeid)
        return i, packet

    return parse_op(bits, i + 6, version, typeid)

def parse(bits):
    i = 0
    packets = []
    while True:
        i, packet = parse_packet(bits, i)
        if not packet:
            break
        packets.append(packet)
    return packets

def sum_versions(packets):
    c = 0
    for p in packets:
        c += p['version']
        if 'packets' in p:
            c += sum_versions(p['packets'])
    return c

def cmd(op, args):
    if op == 0:
        return sum(args)
    if op == 1:
        return prod(args)
    if op == 2:
        return min(args)
    if op == 3:
        return max(args)
    if op == 5:
        return int(args[0] > args[1])
    if op == 6:
        return int(args[0] < args[1])
    if op == 7:
        return int(args[0] == args[1])
    raise 'unknown op ' + str(op)

def cmd_desc(op):
    if op == 0:
        return 'sum'
    if op == 1:
        return 'prod'
    if op == 2:
        return 'min'
    if op == 3:
        return 'max'
    if op == 5:
        return 'greater'
    if op == 6:
        return 'less'
    if op == 7:
        return 'equal'
    raise 'unknown op ' + str(op)

def calc_packets(packets, depth=0):
    values = []
    for p in packets:
        print(' * '*depth, 'type', p['type'], 'version', p['version'])
        if p['type'] == 4:
            print(' - '*depth, 'op', 'literal', 'val', ' -> ', p['value'])
            values.append(p['value'])
        else:
            vals = calc_packets(p['packets'], depth+1)
            v = cmd(p['type'], vals)
            print(' - '*depth, 'op', cmd_desc(p['type']), 'vals', vals, ' -> ', v)
            values.append(v)
    return values

if __name__=='__main__':
    bits = sys.stdin.readline().strip()
    print('bits', bits)
    packets = parse(bits)
    print()
    #cnt = sum_versions(packets) # part 1
    values = calc_packets(packets)
    print('values', values)
