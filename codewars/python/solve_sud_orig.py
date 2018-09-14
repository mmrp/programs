#!/usr/bin/python
import copy
import math
def solve(board, rows, cols, boxes, cr, R, S):
    #print "================="
    #print rows
    #print cols
    #print boxes
    if cr == R:
        return True

    if 0 not in board[cr]:
        return solve(board, copy.deepcopy(rows), copy.deepcopy(cols), copy.deepcopy(boxes), cr + 1, R, S)

    cc = board[cr].index(0)
    b = S * (cr / S) + cc / S #S * (cr / S) + cc / S    #box number
#    print cr, cc, b
    for e in rows[cr]:
        if e not in cols[cc] or e not in boxes[b]:
            continue
        board[cr][cc] = e
#        print e
        nb = copy.deepcopy(boxes)
        nr = copy.deepcopy(rows)
        nc = copy.deepcopy(cols)
        nb[b].remove(e)
        nr[cr].remove(e)
        nc[cc].remove(e)
        if solve(board, nr, nc, nb, cr, R, S):
            return True
        board[cr][cc] = 0
    return False



from sudoku import validSolution
def sudoku(board):
    r = len(board)
    c = len(board[0])
    s = int(math.sqrt(r))
    n = set([i for i in range(r + 1)])
    z = set([0])
    rows  = [list(n - set(e) - z) for e in board]
    cols  = [list(n - set(e) - z) for e in zip(*board)]
    boxes = [list(n - set([board[a+i][b+j] for i in range(s) for j in range(s)]) - z) for a in 
            range(0, r, s) for b in range(0, r, s)]
    #print rows
    print cols
    #print boxes
    r = solve(board, rows, cols, boxes, 0, r, s)
    if validSolution(board):
        print "Valid"
        print_board(board)
    else:
        print "Invalid solution"

def print_board(board):
    for r in board:
        for c in r:
            print c,
        print

puzzle = [[5,3,0,0,7,0,0,0,0],
          [6,0,0,1,9,5,0,0,0],
          [0,9,8,0,0,0,0,6,0],
          [8,0,0,0,6,0,0,0,3],
          [4,0,0,8,0,3,0,0,1],
          [7,0,0,0,2,0,0,0,6],
          [0,6,0,0,0,0,2,8,0],
          [0,0,0,4,1,9,0,0,5],
          [0,0,0,0,8,0,0,7,9]]

sudoku(puzzle)
