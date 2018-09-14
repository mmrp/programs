#!/usr/bin/python

from itertools import *
import copy
import math
rows='ABCDEFGHI'
cols='123456789'
def prune(nbrs, values, idx, v, check = False):
    for n in nbrs[idx]:
        if v in values[n]:
            values[n].remove(v)
            if check and len(values[n]) == 0:
                return False
    values[idx]=[]
    return True

def solve_sud(nbrs, values, board):
    marr = [(len(values[k]), k) for k in values if len(values[k]) != 0]
    if not marr:
        print "Solved"
        return True

    l, idx = min(marr)
    for v in values[idx]:
        new_nbrs = copy.deepcopy(nbrs)
        new_values = copy.deepcopy(values)
        if not prune(new_nbrs, new_values, idx, v, True):
            continue
        r = rows.index(idx[0])
        c = cols.index(idx[1])
        board[r][c] = v
        if solve_sud(new_nbrs, new_values, board):
            return True
        board[r][c] = 0
    return False

def solve(board):
    nbrs = {}
    values = {}
    for i, r in enumerate(rows):
        for j, c in enumerate(cols):
            ci = r + c
            br = 3 * (i / 3)
            bc = 3 * (j / 3)
            nbrs[ci] =  set([''.join(p) for p in product(rows, c)] + \
                        [''.join(p) for p in product(r, cols)] + \
                        [''.join(p) for p in product(rows[br: br + 3], cols[bc: bc + 3])]) - set([ci]) 
            values[ci] = [k for k in range(1, 10)]

    for i, r in enumerate(rows):
        for j, c in enumerate(cols):
            ci = r + c
            if board[i][j] != 0:
                prune(nbrs, values, ci, board[i][j], False)
    print values
    import time
    t1 = time.time()
    if solve_sud(nbrs, values, board):
        print_board(board)
    t2 = time.time()
    print(t2-t1)

def print_board(board):
    r = len(board)
    s = int(math.sqrt(r))
    vlist = [i for i in range(0, r+1, s)]
    line = ' ' + '+'.join(['-' * (2*s) for i in range(s)])
    for i in range(r):
        if i in vlist:
            print line
        print ''.join(('|' if j in vlist else '') + str(board[i][j]) + ' ' for j in range(r)) + '|'

    print line


#    print nbrs
#    print values
puzzle = [[5,3,0,0,7,0,0,0,0],
          [6,0,0,1,9,5,0,0,0],
          [0,9,8,0,0,0,0,6,0],
          [8,0,0,0,6,0,0,0,3],
          [4,0,0,8,0,3,0,0,1],
          [7,0,0,0,2,0,0,0,6],
          [0,6,0,0,0,0,2,8,0],
          [0,0,0,4,1,9,0,0,5],
          [0,0,0,0,8,0,0,7,9]]

puzzle1=[[8,5,0,0,0,2,4,0,0],
         [7,2,0,0,0,0,0,0,9],
         [0,0,4,0,0,0,0,0,0],
         [0,0,0,1,0,7,0,0,2],
         [3,0,5,0,0,0,9,0,0],
         [0,4,0,0,0,0,0,0,0],
         [0,0,0,0,8,0,0,7,0],
         [0,1,7,0,0,0,0,0,0],
         [0,0,0,0,3,6,0,4,0]]

puzzle2=[[9, 0, 0, 0, 8, 0, 0, 0, 1],
 [0, 0, 0, 4, 0, 6, 0, 0, 0],
 [0, 0, 5, 0, 7, 0, 3, 0, 0],
 [0, 6, 0, 0, 0, 0, 0, 4, 0],
 [4, 0, 1, 0, 6, 0, 5, 0, 8],
 [0, 9, 0, 0, 0, 0, 0, 2, 0],
 [0, 0, 7, 0, 3, 0, 2, 0, 0],
 [0, 0, 0, 7, 0, 5, 0, 0, 0],
 [1, 0, 0, 0, 4, 0, 0, 0, 7]]
solve(puzzle)
solve(puzzle1)
solve(puzzle2)

