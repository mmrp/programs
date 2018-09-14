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
    values[idx] = []								
    return True

def solve_sud(nbrs, values, board, sols, tryall):
    lst = [(len(values[k]), k) for k in values if len(values[k]) != 0]
    if not lst:
        sols.append(copy.deepcopy(board))
        if len(sols) == 2:					# more than one solution abort
        	raise Exception()
        return True
	
    l, idx = min(lst)
    r = rows.index(idx[0])
    c = cols.index(idx[1])

    for v in values[idx]:
        new_values = copy.deepcopy(values)
        if not prune(nbrs, new_values, idx, v, True):	# if current assignment leads to a non-solution, skip
            continue

        board[r][c] = v
        if solve_sud(nbrs, new_values, board, sols, tryall) and not tryall:		
        	return True
            
        board[r][c] = 0


import sys
def sudoku_solver(board):
    print board
    sys.stdout.flush()
    nbrs = {}
    values = {}
    if len(board) != 9 and len(board[0]) != 9:
    	raise Exception()
        
    for i, r in enumerate(rows):
        for j, c in enumerate(cols):
            ci = r + c
            br = 3 * (i / 3)
            bc = 3 * (j / 3)
            nbrs[ci] =  set([''.join(p) for p in product(rows, c)] + \
                        [''.join(p) for p in product(r, cols)] + \
                        [''.join(p) for p in product(rows[br: br + 3], cols[bc: bc + 3])]) - set([ci])
            values[ci] = [q for q in range(1, 10)]
            
	non_empty = 0
    for i, r in enumerate(rows):
        for j, c in enumerate(cols):
            ci = r + c
            v = board[i][j]
            if v < 0 or v > 9:
            	raise Exception()
                
            if v != 0:
            	non_empty += 1
                if v in values[ci]:
                    prune(nbrs, values, ci, board[i][j], False)
                else:
                    print "Invalid solution"
                    raise Exception()
                    
	for i, r in enumerate(rows):
		for j, c in enumerate(cols):
			if board[i][j] == 0 and not values[r + c]: 
				raise Exception()
                
    import time
    t1 = time.time()
    
    sols=[]
    solve_sud(nbrs, values, board, sols, non_empty != 17)
    
    if len(sols) == 0:
        print "No Solutions possible"
        raise Exception()
        
    t2 = time.time()
    print(t2-t1)
    return sols[0]
