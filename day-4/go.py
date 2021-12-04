#!/usr/bin/env python3

import sys

class Grid:
    def __init__(self, board):
        self.board = board
        self.marked = list([list([0 for _ in range(5)]) for _ in range(5)])
        self.steps = 0
        self.last_num = None

    def pmarked(self):
        print()
        for row in self.marked:
            print(' '.join(map(str, row)))

    def pboard(self):
        print()
        for row in self.board:
            print(' '.join(map(str, row)))

    def mark_num(self, num):
        self.steps += 1
        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                if self.board[i][j] == num:
                    self.marked[i][j] = 1
                    self.last_num = num

    def is_bingo(self):
        for row in self.marked:
            if sum(row) == len(row):
                return True
        for i in range(len(self.marked[0])):
            col = list(map(lambda r: r[i], self.marked))
            if sum(col) == len(col):
                return True
        return False

    def sum_unmarked(self):
        count = 0
        for i in range(len(self.marked)):
            for j in range(len(self.marked[i])):
                if self.marked[i][j] == 0:
                    count += self.board[i][j]
        return count

    def apply_drawing(self, drawing):
        for n in drawing:
            self.mark_num(n)
            if self.is_bingo():
                return True


def find_winner(grids, drawing):
    for num in drawing:
        for g in grids:
            g.mark_num(num)
            g.pmarked()
            if g.is_bingo():
                print('bingo!')
                return g
    return None

def find_loser(grids, drawing):
    last_bingo = None
    bingo_grids = []
    for num in drawing:
        for g in grids:
            g.mark_num(num)

            if g.is_bingo():
                last_bingo = g
                bingo_grids.append(g)

        for g in bingo_grids:
            grids.remove(g) # should copy, not mutate input
        bingo_grids = []
    return last_bingo


if __name__=='__main__':
    lines = []
    drawing = list(map(int, sys.stdin.readline().split(',')))
    print(drawing)

    grids = []
    i = 0

    ary = []
    for line in sys.stdin.readlines():
        if (line == '\n'):
            continue

        row = list(map(int, line.split()))
        ary.append(row)
        if len(ary) == 5:
            g = Grid(ary)
            grids.append(g)
            ary = []

    #print(list(map(lambda g: g.pboard(), grids)))
    # winner = find_winner(grids, drawing)
    # winner.pmarked()
    # print('score:', winner.sum_unmarked() * winner.last_num)

    loser = find_loser(grids, drawing)
    print('sum', loser.sum_unmarked(), 'last_num', loser.last_num)
    print('score:', loser.sum_unmarked() * loser.last_num)
