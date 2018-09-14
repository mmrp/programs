#!/usr/bin/python
from itertools import *
import copy
import math
rows='ABCDEFGHI'
cols='123456789'
def prune(nbrs, values, idx, v, check = True):
    for n in nbrs[idx]:
        if v in values[n]:
            values[n].remove(v)
            if check and len(values[n]) == 0:   #Filling a position, leaves a neighbor
                return False                    #with zero options, notify to upper layer
    values[idx]=[]
    return True

def solve_sud(nbrs, values, board, sols):
    lst = [(len(values[k]), k) for k in values if len(values[k]) != 0]
    if not lst:
        sols.append(copy.deepcopy(board))
        return 
	
    l, idx = min(lst)
    r = rows.index(idx[0])
    c = cols.index(idx[1])

    for v in values[idx]:
        new_values = copy.deepcopy(values)
        if not prune(nbrs, new_values, idx, v, True):
            continue

        board[r][c] = v
        solve_sud(nbrs, new_values, board, sols)
        board[r][c] = 0

    #return count == 1
    return
    
def sudoku_solver(board):
    print board
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
            values[ci] = [q for q in range(1, 10)]

    for i, r in enumerate(rows):
        for j, c in enumerate(cols):
            ci = r + c
            v = board[i][j]
            if v != 0:
                if v in values[ci]:
                    prune(nbrs, values, ci, board[i][j], False)
                else:
                    print "Invalid solution"
                    raise Exception()
    for i, r in enumerate(rows):
        for j, c in enumerate(cols):
            if not board[i][j] and not values[r+c]: # board(pos) is an empty but has zero possibilies, error
                raise Exception()
    import time
    t1 = time.time()
    sols=[]
    solve_sud(nbrs, values, board, sols)
    if len(sols) != 1:
        print "No Solutions possible"
        raise Exception()
    t2 = time.time()
    print(t2-t1)
    return sols[0] 

puzzle = [[0, 0, 6, 1, 0, 0, 0, 0, 8], 
          [0, 8, 0, 0, 9, 0, 0, 3, 0], 
          [2, 0, 0, 0, 0, 5, 4, 0, 0], 
          [4, 0, 0, 0, 0, 1, 8, 0, 0], 
          [0, 3, 0, 0, 7, 0, 0, 4, 0], 
          [0, 0, 7, 9, 0, 0, 0, 0, 3], 
          [0, 0, 8, 4, 0, 0, 0, 0, 6], 
          [0, 2, 0, 0, 5, 0, 0, 8, 0], 
          [1, 0, 0, 0, 0, 2, 5, 0, 0]]

solution = [[3, 4, 6, 1, 2, 7, 9, 5, 8], 
            [7, 8, 5, 6, 9, 4, 1, 3, 2], 
            [2, 1, 9, 3, 8, 5, 4, 6, 7], 
            [4, 6, 2, 5, 3, 1, 8, 7, 9], 
            [9, 3, 1, 2, 7, 8, 6, 4, 5], 
            [8, 5, 7, 9, 4, 6, 2, 1, 3], 
            [5, 9, 8, 4, 1, 3, 7, 2, 6],
            [6, 2, 4, 7, 5, 9, 3, 8, 1],
            [1, 7, 3, 8, 6, 2, 5, 9, 4]]

uns=[[0, 2, 3, 4, 5, 6, 7, 8, 9], 
     [1, 5, 6, 7, 8, 9, 0, 2, 3], 
     [7, 8, 9, 1, 2, 3, 4, 5, 6], 
     [2, 3, 4, 5, 6, 7, 8, 9, 1], 
     [5, 6, 7, 8, 9, 1, 2, 3, 4], 
     [8, 9, 1, 2, 3, 4, 5, 6, 7], 
     [3, 4, 5, 6, 7, 8, 9, 1, 2], 
     [6, 7, 8, 9, 1, 2, 3, 4, 5], 
     [9, 1, 2, 3, 4, 5, 6, 7, 8]]

hard=[[0, 0, 0, 0, 0, 2, 7, 5, 0], [0, 1, 8, 0, 9, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [4, 9, 0, 0, 0, 0, 0, 0, 0], [0, 3, 0, 0, 0, 0, 0, 0, 8], [0, 0, 0, 7, 0, 0, 2, 0, 0], [0, 0, 0, 0, 3, 0, 0, 0, 9], [7, 0, 0, 0, 0, 0, 0, 0, 0], [5, 0, 0, 0, 0, 0, 0, 8, 0]]
hard1=[[8, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 3, 6, 0, 0, 0, 0, 0], [0, 7, 0, 0, 9, 0, 2, 0, 0], [0, 5, 0, 0, 0, 7, 0, 0, 0], [0, 0, 0, 0, 4, 5, 7, 0, 0], [0, 0, 0, 1, 0, 0, 0, 3, 0], [0, 0, 1, 0, 0, 0, 0, 6, 8], [0, 0, 8, 5, 0, 0, 0, 1, 0], [0, 9, 0, 0, 0, 0, 4, 0, 0]]
print sudoku_solver(hard1)
#, solution)
