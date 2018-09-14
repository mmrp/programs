#!/usr/bin/python
import sys
import itertools, copy
from itertools import product

def forward(s):
    g = s[0]
    c = 1
    for i in s:
        if i > g:
            c += 1
            g = i
    return c

def backward(s):
    return forward(s[::-1])


n = 6
import sys
import itertools
perm_all = {(forward(e), backward(e)): [list(e)] for e in list(itertools.permutations(range(1, n+1)))}
for i in range(n+1):
    v = []
    for j in range(n+1):
        if (i, j) in perm_all:
            for e in perm_all[(i, j)]:
                v.append(e)
    if v:
        perm_all[(i,0)] = v
    

for e in sorted(perm_all.keys()):
    print(e, perm_all[e])

def check_board(square, cclues, n):
    for col in range(n):
        cd, cu = cclues[col]
        s  = [square[row][col] for row in range(n)]

        if cd and cd != forward(s):
            return False

        if cu and cu != forward(s[::-1]):
            return False
    
    return True


def solve_rec(board, row, rclues, cclues, n):
    print(board)
    if row == n: return check_board(board, cclues, n)
    rc = rclues[row]
    for e in perm_all[rc]:
        print row, e
        board[row] = e 
        if solve_rec(board, row + 1, rclues, cclues, n):
            return True
    return False    
        
     
def solve(clues):
    n = len(clues)/4
    board = [[] for _ in range(n)]
    rclues = [(clues[4*n-1-i], clues[n+i]) for i in range(n)] #top and bottom
    cclues = [(clues[0+i], clues[3*n-1-i]) for i in range(n)] #left and right

    if solve_rec(board, 0, rclues, cclues, n):
          return tuple(tuple(r) for r in board)

import time
for c in ([ 3, 2, 2, 3, 2, 1, 1, 2, 3, 3, 2, 2, 5, 1, 2, 2, 4, 3, 3, 2, 1, 2, 2, 4 ],
          [ 0, 3, 0, 5, 3, 4, 0, 0, 0, 0, 0, 1, 0, 3, 0, 3, 2, 3, 3, 2, 0, 3, 1, 0 ],
          [ 0, 0, 0, 2, 2, 0, 0, 0, 0, 6, 3, 0, 0, 4, 0, 0, 0, 0, 4, 4, 0, 3, 0, 0 ]):
#    clues = [2, 2, 1, 3, 2, 2, 3, 1, 1, 2, 2, 3, 3, 2, 1, 3]
    #c = [0, 0, 2, 1, 0, 0, 0, 5, 0, 0, 0, 0, 1, 0, 2, 0, 0, 0, 4, 4]
    t1 = time.time()
    print(solve(c))
    t2 = time.time()
    print(t2 - t1) 
    break
