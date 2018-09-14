#!/usr/bin/python
import sys
import itertools, copy
from itertools import product


def check_board(square, rcond, ccond, rs, re, n, rowCheck = False, colCheck = False):
    if rowCheck:
        for row in range(rs, re+1):
            rf, rb  = rcond[row]
            if rf and rf != forward(square[row]):
                return False
        
            if rb and rb != forward(square[row][::-1]):
                return False

    if not colCheck:
        return True

    for col in range(n):
        cd, cu = ccond[col]
        s  = [square[row][col] for row in range(n)]

        if cd and cd != forward(s):
            return False

        if cu and cu != forward(s[::-1]):
            return False
    
    return True

def prune(row, values, v, n):
    # check all the remaining rows entries from row+1
    # check each entry of a row
    # if an entry element of a position matches with corresponding in v remove it
    for r in range(row+1, n):
        for cp, ce in enumerate(v):
            g = values[r]
            for i in range(len(g)-1, -1, -1):
                if g[i][cp] == ce:
                    g.pop(i)
            if len(g) == 0: return False 

    for c in range(n):
        g = values[c+n]
        for i in range(len(g)-1, -1, -1):
            if g[i][row] != v[c]:
                g.pop(i)
            if len(g) == 0: return False 

    return True


def solve_rec(rows, values, board, n):
    if not rows: return True

    r = [(len(values[r]), r) for r in rows if values[r] != 0]
    print('rows r', r)
    r = min(r)[1]
#    return
    
    for v in values[r]:
#        print 'trying with : ', row, v
        newvalues = copy.deepcopy(values)
        if not prune(r, newvalues, v, n): continue 

        board[r] = v
        nrows = copy.deepcopy(rows) 
        nrows.remove(r)
        if solve_rec(nrows, newvalues, board, n): return True
        
        board[r] = [0] * n  

    return False    
        
     
def solve(clues):
    n = len(clues)/4
    board = [[0] * n for _ in range(n)]
    rclues = [(clues[4*n-1-i], clues[n+i]) for i in range(n)] #top and bottom
    cclues = [(clues[0+i], clues[3*n-1-i]) for i in range(n)] #left and right
    if 0:
        print('clues')
        for e in rclues: print(e)
        for e in cclues: print(e)
    values = {}
    #store possible permutations of rows (clues) from 0 to n-1 and cols from n to 2*n-1
    for i in range(n):
        values[i]   =  copy.deepcopy(perm_all[rclues[i]])
        values[n+i] =  copy.deepcopy(perm_all[cclues[i]])
    if 0:
        print 'values'
        for e in values.keys(): 
            print  e, values[e]
    rows = range(6)
    if solve_rec(rows, values, board, n):
          return tuple(tuple(r) for r in board)

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
perm_all = {}
for e in list(itertools.permutations(range(1, n+1))):
    v = (forward(e), backward(e))
    if v not in perm_all:
        perm_all[v] = []
    perm_all[v].append(e)

z = []
for i in range(1, n+1):
    v = []
    for j in range(1, n+1):
        if (i, j) in perm_all:
            for e in perm_all[(i, j)]:
                v.append(e)
    if v: 
        perm_all[(i, 0)] = v
        z += v

for i in range(1, n+1):
    v = []
    for j in range(1, n+1):
        if (j, i) in perm_all:
            for e in perm_all[(j, i)]:
                v.append(e)
    if v: 
        perm_all[(0, i)] = v
        z += v
        
perm_all[(0,0)] = z
 

#for e in perm_all: print(e, perm_all[e])
import time
for c in ([ 3, 2, 2, 3, 2, 1, 1, 2, 3, 3, 2, 2, 5, 1, 2, 2, 4, 3, 3, 2, 1, 2, 2, 4 ],
          [ 0, 3, 0, 5, 3, 4, 0, 0, 0, 0, 0, 1, 0, 3, 0, 3, 2, 3, 3, 2, 0, 3, 1, 0 ],
          [ 0, 0, 0, 2, 2, 0, 0, 0, 0, 6, 3, 0, 0, 4, 0, 0, 0, 0, 4, 4, 0, 3, 0, 0 ]):
#    c = [0, 0, 1, 3, 2, 0, 3, 0, 0, 0, 0, 3, 0, 2, 1, 3] 
    #c = [2, 2, 1, 3, 2, 2, 3, 1, 1, 2, 2, 3, 3, 2, 1, 3]
    #c = [0, 0, 2, 1, 0, 0, 0, 5, 0, 0, 0, 0, 1, 0, 2, 0, 0, 0, 4, 4]
    t1 = time.time()
    print(solve(c))
    t2 = time.time()
    print(t2 - t1) 
    #break
