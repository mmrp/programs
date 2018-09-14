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

def get_set(perm, a1, a2, n):
    s = [set([]) for _ in range(n)]
    if not(a1) and not(a2):
        return [set(range(1,n+1)) for _ in range(n)]

    for e in perm:
        l = perm[e]
        f, b = e
        if (not(a1) and b == a2) or (f == a1 and not(a2)) or (f == a1 and b == a2):
            for g in l:
                for p, v in enumerate(g):
                    s[p].add(v)
       
    return s if all(s) else []

n = 6
perm_all = {}
for e in list(itertools.permutations(range(1, n+1))):
    v = (forward(e), backward(e))
    if v not in perm_all:
        perm_all[v] = []
    perm_all[v].append(e)


mapping = {}
for i in range(n+1):
    for j in range(n+1):
        r = get_set(perm_all, i, j, n)
        if r: mapping[(i, j)] = r

for e in mapping: print e, mapping[e]

def check_board(square, rclues, cclues, rs, re, n, rowCheck = False, colCheck = False):
    if rowCheck:
        for row in range(rs, re+1):
            rf, rb  = rclues[row]
            if rf and rf != forward(square[row]):
                return False
        
            if rb and rb != forward(square[row][::-1]):
                return False

    if not colCheck:
        return True

    for col in range(n):
        cd, cu = cclues[col]
        s  = [square[row][col] for row in range(n)]

        if cd and cd != forward(s):
            return False

        if cu and cu != forward(s[::-1]):
            return False
    
    return True




ROWS='ABCDEFG'
COLS='1234567'


def prune(nbrs, values, board, r, c, idx, v):
    for n in nbrs[idx]:
        if v in values[n]:
            values[n].remove(v)
            if len(values[n]) == 0:
                return False           
    values[idx] = []								
    return True


def valid(board, _row, _col, _rclue, _cclue, _val):
    pass 

def solve_rec(nbrs, values, board, rclues, cclues, n):
    minlist = [(len(values[k]), k) for k in values if len(values[k]) != 0]
     
    if not minlist:
        return True

    l, p = min(minlist)
    r = ROWS.index(p[0])
    c = COLS.index(p[1])
     
    for v in values[p]:
        if not valid(board, r, c, rclues[r], cclues[c], v): 
            continue

        newvalues = copy.deepcopy(values)
        if not prune(nbrs, newvalues, board, r, c, p, v):
            board[r][c] = 0
            continue 
        
        board[r][c] = v
        if solve_rec(nbrs, newvalues, board, rclues, cclues, n):
            return True
            
        board[r][c] = 0 
    return False    
        
     
def solve(clues):
    n = len(clues)/4
    board = [[0] * n for _ in range(n)]
    rclues = [(clues[4*n-1-i], clues[n+i]) for i in range(n)] #top and bottom
    cclues = [(clues[0+i], clues[3*n-1-i]) for i in range(n)] #left and right

    nbrs = {}
    values = {}
    rows = ROWS[:n]
    cols = COLS[:n]
    for i, r in enumerate(rows):
        rv  = mapping[rclues[i]] 
        for j, c in enumerate(cols):
            nbrs[r+c] =  list(set([''.join(p) for p in product(rows, c)]  + \
                                  [''.join(p) for p in product(r, cols)] \
                                 ) - set([r+c])
                             )
            cv  = mapping[cclues[j]] 
            values[r+c] =  rv[j] & cv[i]
   
    while True:
        g =  [(len(values[r]), r) for r in values if len(values[r]) != 0]
        print(g)
        l , r = min(g)
        print('checking', l, values[r])
        if l != 1:
            break
        if not prune(nbrs, values, board, 0, 0, r, list(values[r])[0]):
            return False

    for e in values.keys():
        print(e, values[e])
    for e in sorted(perm_all.keys()):
        print(e, perm_all[e])
    sys.exit(0);
    if solve_rec(nbrs, values, board, rclues, cclues, n):
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
    #break
