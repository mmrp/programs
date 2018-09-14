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

def solve_sud(nbrs, values, board):
    lst = [(len(values[k]), k) for k in values if len(values[k]) != 0]
   
    count = 0
    if not lst:
        print_board(board)
        print values
        return 

    l, idx = min(lst)
    r = rows.index(idx[0])
    c = cols.index(idx[1])

    for v in values[idx]:
        new_values = copy.deepcopy(values)
        if not prune(nbrs, new_values, idx, v, True):  
            continue
        
        board[r][c] = v
        if solve_sud(nbrs, new_values, board):
            count += c
            #return count
        
#            return True

        board[r][c] = 0
    
#    return count 

from sudoku import validSolution
"""
- Create a list of neighbours i.e 19 for each position in a 9x9 grid
- Try possible values for each position, choose positions with total minimal possibities
    - for each possible value of a position, prune the neighbour possibilities
- If all possible values are exhausted 

"""
def solve(board):
    print "-" * 100
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
    import time
    t1 = time.time()
    solve_sud(nbrs, values, board)
    count = 0
    if count:
        print count
        if validSolution(board):
            print "Valid"
            print_board(board)
        else:
            print "invalid"
    else:
        print "No Solutions possible"
#        raise Exception()
    t2 = time.time()
    print(t2-t1)
    return board

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
one=[[0, 0, 6, 1, 0, 0, 0, 0, 8], [0, 8, 0, 0, 9, 0, 0, 3, 0], [2, 0, 0, 0, 0, 5, 4, 0, 0], [4, 0, 0, 0, 0, 1, 8, 0, 0], [0, 3, 0, 0, 7, 0, 0, 4, 0], [0, 0, 7, 9, 0, 0, 0, 0, 3], [0, 0, 8, 4, 0, 0, 0, 0, 6], [0, 2, 0, 0, 5, 0, 0, 8, 0], [1, 0, 0, 0, 0, 2, 5, 0, 0]]
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
puzzle3=[[9, 8, 0, 0, 8, 0, 0, 0, 1],
 [0, 0, 0, 4, 0, 6, 0, 0, 0],
 [0, 0, 5, 0, 7, 0, 3, 0, 0],
 [0, 6, 0, 0, 0, 0, 0, 4, 0],
 [4, 0, 1, 0, 6, 0, 5, 0, 8],
 [0, 9, 0, 0, 0, 0, 0, 2, 0],
 [0, 0, 7, 0, 3, 0, 2, 0, 0],
 [0, 0, 0, 7, 0, 5, 0, 0, 0],
 [1, 0, 0, 0, 4, 0, 0, 0, 7]]
puzzle4= [[1, 1, 3, 4, 5, 6, 7, 8, 9],
          [4, 0, 6, 7, 8, 9, 1, 2, 3], 
          [7, 8, 9, 1, 2, 3, 4, 5, 6], 
          [2, 3, 4, 5, 6, 7, 8, 9, 1], 
          [5, 6, 7, 8, 9, 1, 2, 3, 4], 
          [8, 9, 1, 2, 3, 4, 5, 6, 7], 
          [3, 4, 5, 6, 7, 8, 9, 1, 2], 
          [6, 7, 8, 9, 1, 2, 3, 4, 5], 
          [9, 1, 2, 3, 4, 5, 6, 7, 8]]
puzzle5= [[0, 2, 3, 4, 5, 6, 7, 8, 9], 
         [1, 5, 6, 7, 8, 9, 0, 2, 3], 
         [7, 8, 9, 1, 2, 3, 4, 5, 6], 
         [2, 3, 4, 5, 6, 7, 8, 9, 1], 
         [5, 6, 7, 8, 9, 1, 2, 3, 4], 
         [8, 9, 1, 2, 3, 4, 5, 6, 7], 
         [3, 4, 5, 6, 7, 8, 9, 1, 2], 
         [6, 7, 8, 9, 1, 2, 3, 4, 5], 
         [9, 1, 2, 3, 4, 5, 6, 7, 8]]
puzzle6=[[0, 0, 3, 4, 5, 6, 7, 8, 9], [4, 5, 6, 7, 8, 9, 0, 0, 3], [7, 8, 9, 0, 0, 3, 4, 5, 6], [0, 3, 4, 5, 6, 7, 8, 9, 0], [5, 6, 7, 8, 9, 0, 0, 3, 4], [8, 9, 0, 0, 3, 4, 5, 6, 7], [3, 4, 5, 6, 7, 8, 9, 0, 0], [6, 7, 8, 9, 0, 0, 3, 4, 5], [9, 0, 0, 3, 4, 5, 6, 7, 8]]
solve(one)
solve(puzzle)
solve(puzzle1)
solve(puzzle2)
#solve(puzzle3)
#solve(puzzle4)
print "puzzle5"
solve(puzzle5)
solve(puzzle6)
